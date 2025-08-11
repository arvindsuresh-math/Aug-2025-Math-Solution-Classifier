import requests
from bs4 import BeautifulSoup
import argparse
import re
from pathlib import Path
from urllib.parse import urlparse
import time
import html2text

def clean_filename(url):
    """Convert URL to a clean filename."""
    parsed = urlparse(url)
    # Extract the model name from the URL path
    model_name = parsed.path.strip('/').replace('/', '_')
    if not model_name:
        model_name = "huggingface_page"
    return f"{model_name}.md"

def scrape_huggingface_page(url):
    """
    Scrape a Hugging Face model page and convert to markdown.
    Returns the markdown content as a string.
    """
    try:
        # Add headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"Fetching content from: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for element in soup(["script", "style", "nav", "footer", "aside"]):
            element.decompose()
        
        # Remove common navigation and header elements (Hugging Face specific)
        for element in soup.find_all(class_=re.compile("header|nav|footer|sidebar|menu", re.I)):
            element.decompose()
            
        # Remove advertisement or promotional content
        for element in soup.find_all(class_=re.compile("ad|promo|banner", re.I)):
            element.decompose()
        
        # Focus on the main content area if it exists
        main_content = soup.find('main') or soup.find(class_=re.compile("main|content", re.I)) or soup
        
        # Convert to markdown using html2text
        h = html2text.HTML2Text()
        h.ignore_links = False  # Keep links
        h.ignore_images = False  # Keep images  
        h.ignore_emphasis = False  # Keep bold/italic
        h.ignore_tables = False  # Keep tables
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True  # Use unicode characters
        h.escape_all = False  # Don't escape markdown characters
        
        # Convert HTML to markdown
        markdown_content = h.handle(str(main_content))
        
        # Clean up extra whitespace and newlines
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
        markdown_content = markdown_content.strip()
        
        # Add metadata header
        header = f"""# Hugging Face Model Page: {url}

**Scraped on:** {time.strftime("%Y-%m-%d %H:%M:%S")}

---

"""
        
        return header + markdown_content
        
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch the page: {e}")
    except Exception as e:
        raise Exception(f"Error processing the page: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scrape Hugging Face model pages and convert to markdown")
    parser.add_argument("url", help="Hugging Face model page URL")
    parser.add_argument("-o", "--output", help="Output filename (optional, will auto-generate if not provided)")
    
    args = parser.parse_args()
    
    # Validate URL
    if not args.url.startswith(('http://', 'https://')):
        args.url = 'https://' + args.url
    
    if 'huggingface.co' not in args.url:
        print("Warning: URL doesn't appear to be a Hugging Face URL")
    
    # Generate output filename if not provided
    if args.output:
        output_file = Path(args.output)
    else:
        filename = clean_filename(args.url)
        output_file = Path.cwd() / filename
    
    try:
        # Scrape the page
        markdown_content = scrape_huggingface_page(args.url)
        
        # Save to file
        output_file.write_text(markdown_content, encoding='utf-8')
        print(f"Successfully saved markdown content to: {output_file}")
        print(f"File size: {len(markdown_content)} characters")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())