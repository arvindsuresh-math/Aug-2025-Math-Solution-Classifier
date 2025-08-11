# Hugging Face Model Page: https://huggingface.co/docs/transformers/v4.53.1/en/main_classes/trainer#trainer

**Scraped on:** 2025-07-23 08:40:42

---

You are viewing v4.53.1 version. A newer version [v4.53.3](/docs/transformers/v4.53.3/main_classes/trainer) is available.

#  Trainer

The [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) class provides an API for feature-complete training in PyTorch, and it supports distributed training on multiple GPUs/TPUs, mixed precision for [NVIDIA GPUs](https://nvidia.github.io/apex/), [AMD GPUs](https://rocm.docs.amd.com/en/latest/rocm.html), and [`torch.amp`](https://pytorch.org/docs/stable/amp.html) for PyTorch. [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) goes hand-in-hand with the [TrainingArguments](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments) class, which offers a wide range of options to customize how a model is trained. Together, these two classes provide a complete training API.

[Seq2SeqTrainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Seq2SeqTrainer) and [Seq2SeqTrainingArguments](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Seq2SeqTrainingArguments) inherit from the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) and [TrainingArguments](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments) classes and they’re adapted for training models for sequence-to-sequence tasks such as summarization or translation.

##  Trainer

Parameters 

  * **model** ([PreTrainedModel](/docs/transformers/v4.53.1/en/main_classes/model#transformers.PreTrainedModel) or `torch.nn.Module`, _optional_) — The model to train, evaluate or use for predictions. If not provided, a `model_init` must be passed. 
  * **args** ([TrainingArguments](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments), _optional_) — The arguments to tweak for training. Will default to a basic instance of [TrainingArguments](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.TrainingArguments) with the `output_dir` set to a directory named _tmp_trainer_ in the current directory if not provided.
  * **data_collator** (`DataCollator`, _optional_) — The function to use to form a batch from a list of elements of `train_dataset` or `eval_dataset`. Will default to [default_data_collator()](/docs/transformers/v4.53.1/en/main_classes/data_collator#transformers.default_data_collator) if no `processing_class` is provided, an instance of [DataCollatorWithPadding](/docs/transformers/v4.53.1/en/main_classes/data_collator#transformers.DataCollatorWithPadding) otherwise if the processing_class is a feature extractor or tokenizer.
  * **train_dataset** (Union[`torch.utils.data.Dataset`, `torch.utils.data.IterableDataset`, `datasets.Dataset`], _optional_) — The dataset to use for training. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. 

Note that if it’s a `torch.utils.data.IterableDataset` with some randomization and you are training in a distributed fashion, your iterable dataset should either use a internal attribute `generator` that is a `torch.Generator` for the randomization that must be identical on all processes (and the Trainer will manually set the seed of this `generator` at each epoch) or have a `set_epoch()` method that internally sets the seed of the RNGs used.

  * **eval_dataset** (Union[`torch.utils.data.Dataset`, dict[str, `torch.utils.data.Dataset`, `datasets.Dataset`]), _optional_) — The dataset to use for evaluation. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. If it is a dictionary, it will evaluate on each dataset prepending the dictionary key to the metric name.
  * **processing_class** (`PreTrainedTokenizerBase` or `BaseImageProcessor` or `FeatureExtractionMixin` or `ProcessorMixin`, _optional_) — Processing class used to process the data. If provided, will be used to automatically process the inputs for the model, and it will be saved along the model to make it easier to rerun an interrupted training or reuse the fine-tuned model. This supersedes the `tokenizer` argument, which is now deprecated.
  * **model_init** (`Callable[[], PreTrainedModel]`, _optional_) — A function that instantiates the model to be used. If provided, each call to [train()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.train) will start from a new instance of the model as given by this function. 

The function may have zero argument, or a single one containing the optuna/Ray Tune/SigOpt trial object, to be able to choose different architectures according to hyper parameters (such as layer count, sizes of inner layers, dropout probabilities etc).

  * **compute_loss_func** (`Callable`, _optional_) — A function that accepts the raw model outputs, labels, and the number of items in the entire accumulated batch (batch_size * gradient_accumulation_steps) and returns the loss. For example, see the default [loss function](https://github.com/huggingface/transformers/blob/052e652d6d53c2b26ffde87e039b723949a53493/src/transformers/trainer.py#L3618) used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer).
  * **compute_metrics** (`Callable[[EvalPrediction], Dict]`, _optional_) — The function that will be used to compute metrics at evaluation. Must take a [EvalPrediction](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.EvalPrediction) and return a dictionary string to metric values. _Note_ When passing TrainingArgs with `batch_eval_metrics` set to `True`, your compute_metrics function must take a boolean `compute_result` argument. This will be triggered after the last eval batch to signal that the function needs to calculate and return the global summary statistics rather than accumulating the batch-level statistics
  * **callbacks** (List of [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback), _optional_) — A list of callbacks to customize the training loop. Will add those to the list of default callbacks detailed in [here](callback). 

If you want to remove one of the default callbacks used, use the [Trainer.remove_callback()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.remove_callback) method.

  * **optimizers** (`tuple[torch.optim.Optimizer, torch.optim.lr_scheduler.LambdaLR]`, _optional_ , defaults to `(None, None)`) — A tuple containing the optimizer and the scheduler to use. Will default to an instance of `AdamW` on your model and a scheduler given by [get_linear_schedule_with_warmup()](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.get_linear_schedule_with_warmup) controlled by `args`.
  * **optimizer_cls_and_kwargs** (`tuple[Type[torch.optim.Optimizer], dict[str, Any]]`, _optional_) — A tuple containing the optimizer class and keyword arguments to use. Overrides `optim` and `optim_args` in `args`. Incompatible with the `optimizers` argument. 

Unlike `optimizers`, this argument avoids the need to place model parameters on the correct devices before initializing the Trainer.

  * **preprocess_logits_for_metrics** (`Callable[[torch.Tensor, torch.Tensor], torch.Tensor]`, _optional_) — A function that preprocess the logits right before caching them at each evaluation step. Must take two tensors, the logits and the labels, and return the logits once processed as desired. The modifications made by this function will be reflected in the predictions received by `compute_metrics`. 

Note that the labels (second parameter) will be `None` if the dataset does not have them.

Trainer is a simple but feature-complete training and eval loop for PyTorch, optimized for 🤗 Transformers.

Important attributes:

  * **model** — Always points to the core model. If using a transformers model, it will be a [PreTrainedModel](/docs/transformers/v4.53.1/en/main_classes/model#transformers.PreTrainedModel) subclass.
  * **model_wrapped** — Always points to the most external model in case one or more other modules wrap the original model. This is the model that should be used for the forward pass. For example, under `DeepSpeed`, the inner model is wrapped in `DeepSpeed` and then again in `torch.nn.DistributedDataParallel`. If the inner model hasn’t been wrapped, then `self.model_wrapped` is the same as `self.model`.
  * **is_model_parallel** — Whether or not a model has been switched to a model parallel mode (different from data parallelism, this means some of the model layers are split on different GPUs).
  * **place_model_on_device** — Whether or not to automatically place the model on the device - it will be set to `False` if model parallel or deepspeed is used, or if the default `TrainingArguments.place_model_on_device` is overridden to return `False` .
  * **is_in_train** — Whether or not a model is currently running `train` (e.g. when `evaluate` is called while in `train`)

Parameters 

  * **callback** (`type` or [`~transformers.TrainerCallback]`) — A [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback) class or an instance of a [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback). In the first case, will instantiate a member of that class.

Add a callback to the current list of [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback).

A helper wrapper that creates an appropriate context manager for `autocast` while feeding it the desired arguments, depending on the situation.

Parameters 

  * **model** (`nn.Module`) — The model to compute the loss for.
  * **inputs** (`dict[str, Union[torch.Tensor, Any]]`) — The input data for the model.
  * **return_outputs** (`bool`, _optional_ , defaults to `False`) — Whether to return the model outputs along with the loss.
  * **num_items_in_batch** (Optional[torch.Tensor], _optional_) — The number of items in the batch. If num_items_in_batch is not passed,

How the loss is computed by Trainer. By default, all models return the loss in the first element.

Subclass and override for custom behavior. If you are not using `num_items_in_batch` when computing your loss, make sure to overwrite `self.model_accepts_loss_kwargs` to `False`. Otherwise, the loss calculationg might be slightly inacurate when performing gradient accumulation.

A helper wrapper to group together context managers.

Parameters 

  * **language** (`str`, _optional_) — The language of the model (if applicable)
  * **license** (`str`, _optional_) — The license of the model. Will default to the license of the pretrained model used, if the original model given to the `Trainer` comes from a repo on the Hub.
  * **tags** (`str` or `list[str]`, _optional_) — Some tags to be included in the metadata of the model card.
  * **model_name** (`str`, _optional_) — The name of the model.
  * **finetuned_from** (`str`, _optional_) — The name of the model used to fine-tune this one (if applicable). Will default to the name of the repo of the original model given to the `Trainer` (if it comes from the Hub).
  * **tasks** (`str` or `list[str]`, _optional_) — One or several task identifiers, to be included in the metadata of the model card.
  * **dataset_tags** (`str` or `list[str]`, _optional_) — One or several dataset tags, to be included in the metadata of the model card.
  * **dataset** (`str` or `list[str]`, _optional_) — One or several dataset identifiers, to be included in the metadata of the model card.
  * **dataset_args** (`str` or `list[str]`, _optional_) — One or several dataset arguments, to be included in the metadata of the model card.

Creates a draft of a model card using the information available to the `Trainer`.

Setup the optimizer.

We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainer’s init through `optimizers`, or subclass and override this method in a subclass.

Setup the optimizer and the learning rate scheduler.

We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the Trainer’s init through `optimizers`, or subclass and override this method (or `create_optimizer` and/or `create_scheduler`) in a subclass.

Parameters 

  * **num_training_steps** (int) — The number of training steps to do.

Setup the scheduler. The optimizer of the trainer must have been set up either before this method is called or passed as an argument.

Parameters 

  * **eval_dataset** (Union[`Dataset`, dict[str, `Dataset`]), _optional_) — Pass a dataset if you wish to override `self.eval_dataset`. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. If it is a dictionary, it will evaluate on each dataset, prepending the dictionary key to the metric name. Datasets must implement the `__len__` method. 
  * **ignore_keys** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.
  * **metric_key_prefix** (`str`, _optional_ , defaults to `"eval"`) — An optional prefix to be used as the metrics key prefix. For example the metrics “bleu” will be named “eval_bleu” if the prefix is “eval” (default)

Run evaluation and returns metrics.

The calling script will be responsible for providing a method to compute metrics, as they are task-dependent (pass it to the init `compute_metrics` argument).

You can also subclass and override this method to inject custom behavior.

Prediction/evaluation loop, shared by `Trainer.evaluate()` and `Trainer.predict()`.

Works both with or without labels.

Parameters 

  * **inputs** (`dict[str, Union[torch.Tensor, Any]]`) — The inputs and targets of the model.

Returns

`int`

The number of floating-point operations.

For models that inherit from [PreTrainedModel](/docs/transformers/v4.53.1/en/main_classes/model#transformers.PreTrainedModel), uses that method to compute the number of floating point operations for every backward + forward pass. If using another model, either implement such a method in the model or subclass and override this method.

Collects a specified number of batches from the epoch iterator and optionally counts the number of items in the batches to properly scale the loss.

Get all parameter names that weight decay will be applied to.

This function filters out parameters in two ways:

  1. By layer type (instances of layers specified in ALL_LAYERNORM_LAYERS)
  2. By parameter name patterns (containing ‘bias’, or variation of ‘norm’)

Parameters 

  * **eval_dataset** (`str` or `torch.utils.data.Dataset`, _optional_) — If a `str`, will use `self.eval_dataset[eval_dataset]` as the evaluation dataset. If a `Dataset`, will override `self.eval_dataset` and must implement `__len__`. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed.

Returns the evaluation `~torch.utils.data.DataLoader`.

Subclass and override this method if you want to inject some custom behavior.

Returns the learning rate of each parameter from self.optimizer.

Get the number of trainable parameters.

Parameters 

  * **args** (`transformers.training_args.TrainingArguments`) — The training arguments for the training session.

Returns the optimizer class and optimizer parameters based on the training arguments.

Parameters 

  * **param** (`str` or `torch.nn.parameter.Parameter`, _optional_) — The parameter for which optimizer group needs to be returned.

Returns optimizer group for a parameter if given, else returns all optimizer groups for params.

Parameters 

  * **test_dataset** (`torch.utils.data.Dataset`, _optional_) — The test dataset to use. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. It must implement `__len__`.

Returns the test `~torch.utils.data.DataLoader`.

Subclass and override this method if you want to inject some custom behavior.

Calculates total batch size (micro_batch _grad_accum_ dp_world_size).

Note: Only considers DP and TP (dp_world_size = world_size // tp_size).

Get the tensor parallel size from either the model or DeepSpeed config.

Returns the training `~torch.utils.data.DataLoader`.

Will use no sampler if `train_dataset` does not implement `__len__`, a random sampler (adapted to distributed training if necessary) otherwise.

Subclass and override this method if you want to inject some custom behavior.

Parameters 

  * **hp_space** (`Callable[["optuna.Trial"], dict[str, float]]`, _optional_) — A function that defines the hyperparameter search space. Will default to `default_hp_space_optuna()` or `default_hp_space_ray()` or `default_hp_space_sigopt()` depending on your backend.
  * **compute_objective** (`Callable[[dict[str, float]], float]`, _optional_) — A function computing the objective to minimize or maximize from the metrics returned by the `evaluate` method. Will default to `default_compute_objective()`.
  * **n_trials** (`int`, _optional_ , defaults to 100) — The number of trial runs to test.
  * **direction** (`str` or `list[str]`, _optional_ , defaults to `"minimize"`) — If it’s single objective optimization, direction is `str`, can be `"minimize"` or `"maximize"`, you should pick `"minimize"` when optimizing the validation loss, `"maximize"` when optimizing one or several metrics. If it’s multi objectives optimization, direction is `list[str]`, can be List of `"minimize"` and `"maximize"`, you should pick `"minimize"` when optimizing the validation loss, `"maximize"` when optimizing one or several metrics.
  * **backend** (`str` or `~training_utils.HPSearchBackend`, _optional_) — The backend to use for hyperparameter search. Will default to optuna or Ray Tune or SigOpt, depending on which one is installed. If all are installed, will default to optuna.
  * **hp_name** (`Callable[["optuna.Trial"], str]]`, _optional_) — A function that defines the trial/run name. Will default to None.
  * **kwargs** (`dict[str, Any]`, _optional_) — Additional keyword arguments for each backend: 
    * `optuna`: parameters from [optuna.study.create_study](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.create_study.html) and also the parameters `timeout`, `n_jobs` and `gc_after_trial` from [optuna.study.Study.optimize](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.study.Study.html#optuna.study.Study.optimize)
    * `ray`: parameters from [tune.run](https://docs.ray.io/en/latest/tune/api_docs/execution.html#tune-run). If `resources_per_trial` is not set in the `kwargs`, it defaults to 1 CPU core and 1 GPU (if available). If `progress_reporter` is not set in the `kwargs`, [ray.tune.CLIReporter](https://docs.ray.io/en/latest/tune/api/doc/ray.tune.CLIReporter.html) is used.
    * `sigopt`: the parameter `proxies` from [sigopt.Connection.set_proxies](https://docs.sigopt.com/support/faq#how-do-i-use-sigopt-with-a-proxy).

Returns

[`trainer_utils.BestRun` or `list[trainer_utils.BestRun]`]

All the information about the best run or best runs for multi-objective optimization. Experiment summary can be found in `run_summary` attribute for Ray backend.

Launch an hyperparameter search using `optuna` or `Ray Tune` or `SigOpt`. The optimized quantity is determined by `compute_objective`, which defaults to a function returning the evaluation loss when no metric is provided, the sum of all metrics otherwise.

Initializes a git repo in `self.args.hub_model_id`.

Whether or not this process is the local (e.g., on one machine if training in a distributed fashion on several machines) main process.

Whether or not this process is the global main process (when training in a distributed fashion on several machines, this is only going to be `True` for one process).

Parameters 

  * **logs** (`dict[str, float]`) — The values to log.
  * **start_time** (`Optional[float]`) — The start of training.

Log `logs` on the various objects watching training.

Subclass and override this method to inject custom behavior.

Parameters 

  * **split** (`str`) — Mode/split name: one of `train`, `eval`, `test`
  * **metrics** (`dict[str, float]`) — The metrics returned from train/evaluate/predictmetrics: metrics dict

Log metrics in a specially formatted way.

Under distributed environment this is done only for a process with rank 0.

Notes on memory reports:

In order to get memory usage report you need to install `psutil`. You can do that with `pip install psutil`.

Now when this method is run, you will see a report that will include:
    
    
    init_mem_cpu_alloc_delta   =     1301MB
    init_mem_cpu_peaked_delta  =      154MB
    init_mem_gpu_alloc_delta   =      230MB
    init_mem_gpu_peaked_delta  =        0MB
    train_mem_cpu_alloc_delta  =     1345MB
    train_mem_cpu_peaked_delta =        0MB
    train_mem_gpu_alloc_delta  =      693MB
    train_mem_gpu_peaked_delta =        7MB

**Understanding the reports:**

  * the first segment, e.g., `train__`, tells you which stage the metrics are for. Reports starting with `init_` will be added to the first stage that gets run. So that if only evaluation is run, the memory usage for the `__init__` will be reported along with the `eval_` metrics.
  * the third segment, is either `cpu` or `gpu`, tells you whether it’s the general RAM or the gpu0 memory metric.
  * `*_alloc_delta` \- is the difference in the used/allocated memory counter between the end and the start of the stage - it can be negative if a function released more memory than it allocated.
  * `*_peaked_delta` \- is any extra memory that was consumed and then freed - relative to the current allocated memory counter - it is never negative. When you look at the metrics of any stage you add up `alloc_delta` \+ `peaked_delta` and you know how much memory was needed to complete that stage.

The reporting happens only for process of rank 0 and gpu 0 (if there is a gpu). Typically this is enough since the main process does the bulk of work, but it could be not quite so if model parallel is used and then other GPUs may use a different amount of gpu memory. This is also not the same under DataParallel where gpu0 may require much more memory than the rest since it stores the gradient and optimizer states for all participating GPUs. Perhaps in the future these reports will evolve to measure those too.

The CPU RAM metric measures RSS (Resident Set Size) includes both the memory which is unique to the process and the memory shared with other processes. It is important to note that it does not include swapped out memory, so the reports could be imprecise.

The CPU peak memory is measured using a sampling thread. Due to python’s GIL it may miss some of the peak memory if that thread didn’t get a chance to run when the highest memory was used. Therefore this report can be less than reality. Using `tracemalloc` would have reported the exact peak memory, but it doesn’t report memory allocations outside of python. So if some C++ CUDA extension allocated its own memory it won’t be reported. And therefore it was dropped in favor of the memory sampling approach, which reads the current process memory usage.

The GPU allocated and peak memory reporting is done with `torch.cuda.memory_allocated()` and `torch.cuda.max_memory_allocated()`. This metric reports only “deltas” for pytorch-specific allocations, as `torch.cuda` memory management system doesn’t track any memory allocated outside of pytorch. For example, the very first cuda call typically loads CUDA kernels, which may take from 0.5 to 2GB of GPU memory.

Note that this tracker doesn’t account for memory allocations outside of [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)’s `__init__`, `train`, `evaluate` and `predict` calls.

Because `evaluation` calls may happen during `train`, we can’t handle nested invocations because `torch.cuda.max_memory_allocated` is a single counter, so if it gets reset by a nested eval call, `train`’s tracker will report incorrect info. If this [pytorch issue](https://github.com/pytorch/pytorch/issues/16266) gets resolved it will be possible to change this class to be re-entrant. Until then we will only track the outer level of `train`, `evaluate` and `predict` methods. Which means that if `eval` is called during `train`, it’s the latter that will account for its memory usage and that of the former.

This also means that if any other tool that is used along the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) calls `torch.cuda.reset_peak_memory_stats`, the gpu peak memory stats could be invalid. And the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer) will disrupt the normal behavior of any such tools that rely on calling `torch.cuda.reset_peak_memory_stats` themselves.

For best performance you may want to consider turning the memory profiling off for production runs.

Parameters 

  * **metrics** (`dict[str, float]`) — The metrics returned from train/evaluate/predict

Returns

metrics (`dict[str, float]`)

The reformatted metrics

Reformat Trainer metrics values to a human-readable format.

Helper to get number of samples in a `~torch.utils.data.DataLoader` by accessing its dataset. When dataloader.dataset does not exist or has no length, estimates as best it can

Helper to get number of tokens in a `~torch.utils.data.DataLoader` by enumerating dataloader.

Parameters 

  * **callback** (`type` or [`~transformers.TrainerCallback]`) — A [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback) class or an instance of a [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback). In the first case, will pop the first member of that class found in the list of callbacks.

Returns

[TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback)

The callback removed, if found.

Remove a callback from the current list of [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback) and returns it.

If the callback is not found, returns `None` (and no error is raised).

Parameters 

  * **test_dataset** (`Dataset`) — Dataset to run the predictions on. If it is an `datasets.Dataset`, columns not accepted by the `model.forward()` method are automatically removed. Has to implement the method `__len__`
  * **ignore_keys** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.
  * **metric_key_prefix** (`str`, _optional_ , defaults to `"test"`) — An optional prefix to be used as the metrics key prefix. For example the metrics “bleu” will be named “test_bleu” if the prefix is “test” (default)

Run prediction and returns predictions and potential metrics.

Depending on the dataset and your use case, your test dataset may contain labels. In that case, this method will also return metrics, like in `evaluate()`.

Returns: _NamedTuple_ A namedtuple with the following keys:

  * predictions (`np.ndarray`): The predictions on `test_dataset`.
  * label_ids (`np.ndarray`, _optional_): The labels (if the dataset contained some).
  * metrics (`dict[str, float]`, _optional_): The potential dictionary of metrics (if the dataset contained labels).

Prediction/evaluation loop, shared by `Trainer.evaluate()` and `Trainer.predict()`.

Works both with or without labels.

Parameters 

  * **model** (`nn.Module`) — The model to evaluate.
  * **inputs** (`dict[str, Union[torch.Tensor, Any]]`) — The inputs and targets of the model. 

The dictionary will be unpacked before being fed to the model. Most models expect the targets under the argument `labels`. Check your model’s documentation for all accepted arguments.

  * **prediction_loss_only** (`bool`) — Whether or not to return the loss only.
  * **ignore_keys** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.

Returns

tuple[Optional[torch.Tensor], Optional[torch.Tensor], Optional[torch.Tensor]]

A tuple with the loss, logits and labels (each being optional).

Perform an evaluation step on `model` using `inputs`.

Subclass and override to inject custom behavior.

Sets values in the deepspeed plugin based on the Trainer args

Parameters 

  * **commit_message** (`str`, _optional_ , defaults to `"End of training"`) — Message to commit while pushing.
  * **blocking** (`bool`, _optional_ , defaults to `True`) — Whether the function should return only when the `git push` has finished.
  * **token** (`str`, _optional_ , defaults to `None`) — Token with write permission to overwrite Trainer’s original args.
  * **revision** (`str`, _optional_) — The git revision to commit from. Defaults to the head of the “main” branch.
  * **kwargs** (`dict[str, Any]`, _optional_) — Additional keyword arguments passed along to [create_model_card()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.create_model_card).

Upload `self.model` and `self.processing_class` to the 🤗 model hub on the repo `self.args.hub_model_id`.

Parameters 

  * **callback** (`type` or [`~transformers.TrainerCallback]`) — A [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback) class or an instance of a [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback). In the first case, will remove the first member of that class found in the list of callbacks.

Remove a callback from the current list of [TrainerCallback](/docs/transformers/v4.53.1/en/main_classes/callback#transformers.TrainerCallback).

Parameters 

  * **split** (`str`) — Mode/split name: one of `train`, `eval`, `test`, `all`
  * **metrics** (`dict[str, float]`) — The metrics returned from train/evaluate/predict
  * **combined** (`bool`, _optional_ , defaults to `True`) — Creates combined metrics by updating `all_results.json` with metrics of this call

Save metrics into a json file for that split, e.g. `train_results.json`.

Under distributed environment this is done only for a process with rank 0.

To understand the metrics please read the docstring of [log_metrics()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.log_metrics). The only difference is that raw unformatted numbers are saved in the current method.

Will save the model, so you can reload it using `from_pretrained()`.

Will only save from the main process.

Saves the Trainer state, since Trainer.save_model saves only the tokenizer with the model.

Under distributed environment this is done only for a process with rank 0.

Calculates and returns the following values:

  * `num_train_epochs`
  * `num_update_steps_per_epoch`
  * `num_examples`
  * `num_train_samples`
  * `epoch_based`
  * `len_dataloader`
  * `max_steps`

Parameters 

  * **resume_from_checkpoint** (`str` or `bool`, _optional_) — If a `str`, local path to a saved checkpoint as saved by a previous instance of [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer). If a `bool` and equals `True`, load the last checkpoint in _args.output_dir_ as saved by a previous instance of [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer). If present, training will resume from the model/optimizer/scheduler states loaded here.
  * **trial** (`optuna.Trial` or `dict[str, Any]`, _optional_) — The trial run or the hyperparameter dictionary for hyperparameter search.
  * **ignore_keys_for_eval** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions for evaluation during the training.
  * **kwargs** (`dict[str, Any]`, _optional_) — Additional keyword arguments used to hide deprecated arguments

Main training entry point.

Parameters 

  * **model** (`nn.Module`) — The model to train.
  * **inputs** (`dict[str, Union[torch.Tensor, Any]]`) — The inputs and targets of the model. 

The dictionary will be unpacked before being fed to the model. Most models expect the targets under the argument `labels`. Check your model’s documentation for all accepted arguments.

Returns

`torch.Tensor`

The tensor with training loss on this batch.

Perform a training step on a batch of inputs.

Subclass and override to inject custom behavior.

##  Seq2SeqTrainer

Parameters 

  * **eval_dataset** (`Dataset`, _optional_) — Pass a dataset if you wish to override `self.eval_dataset`. If it is an [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. It must implement the `__len__` method.
  * **ignore_keys** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.
  * **metric_key_prefix** (`str`, _optional_ , defaults to `"eval"`) — An optional prefix to be used as the metrics key prefix. For example the metrics “bleu” will be named “eval_bleu” if the prefix is `"eval"` (default)
  * **max_length** (`int`, _optional_) — The maximum target length to use when predicting with the generate method.
  * **num_beams** (`int`, _optional_) — Number of beams for beam search that will be used when predicting with the generate method. 1 means no beam search.
  * **gen_kwargs** — Additional `generate` specific kwargs.

Run evaluation and returns metrics.

The calling script will be responsible for providing a method to compute metrics, as they are task-dependent (pass it to the init `compute_metrics` argument).

You can also subclass and override this method to inject custom behavior.

Parameters 

  * **test_dataset** (`Dataset`) — Dataset to run the predictions on. If it is a [Dataset](https://huggingface.co/docs/datasets/v3.6.0/en/package_reference/main_classes#datasets.Dataset), columns not accepted by the `model.forward()` method are automatically removed. Has to implement the method `__len__`
  * **ignore_keys** (`list[str]`, _optional_) — A list of keys in the output of your model (if it is a dictionary) that should be ignored when gathering predictions.
  * **metric_key_prefix** (`str`, _optional_ , defaults to `"eval"`) — An optional prefix to be used as the metrics key prefix. For example the metrics “bleu” will be named “eval_bleu” if the prefix is `"eval"` (default)
  * **max_length** (`int`, _optional_) — The maximum target length to use when predicting with the generate method.
  * **num_beams** (`int`, _optional_) — Number of beams for beam search that will be used when predicting with the generate method. 1 means no beam search.
  * **gen_kwargs** — Additional `generate` specific kwargs.

Run prediction and returns predictions and potential metrics.

Depending on the dataset and your use case, your test dataset may contain labels. In that case, this method will also return metrics, like in `evaluate()`.

Returns: _NamedTuple_ A namedtuple with the following keys:

  * predictions (`np.ndarray`): The predictions on `test_dataset`.
  * label_ids (`np.ndarray`, _optional_): The labels (if the dataset contained some).
  * metrics (`dict[str, float]`, _optional_): The potential dictionary of metrics (if the dataset contained labels).

##  TrainingArguments

Parameters 

  * **output_dir** (`str`, _optional_ , defaults to `"trainer_output"`) — The output directory where the model predictions and checkpoints will be written.
  * **overwrite_output_dir** (`bool`, _optional_ , defaults to `False`) — If `True`, overwrite the content of the output directory. Use this to continue training if `output_dir` points to a checkpoint directory.
  * **do_train** (`bool`, _optional_ , defaults to `False`) — Whether to run training or not. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **do_eval** (`bool`, _optional_) — Whether to run evaluation on the validation set or not. Will be set to `True` if `eval_strategy` is different from `"no"`. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **do_predict** (`bool`, _optional_ , defaults to `False`) — Whether to run predictions on the test set or not. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **eval_strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"no"`) — The evaluation strategy to adopt during training. Possible values are: 
    * `"no"`: No evaluation is done during training.
    * `"steps"`: Evaluation is done (and logged) every `eval_steps`.
    * `"epoch"`: Evaluation is done at the end of each epoch.
  * **prediction_loss_only** (`bool`, _optional_ , defaults to `False`) — When performing evaluation and generating predictions, only returns the loss.
  * **per_device_train_batch_size** (`int`, _optional_ , defaults to 8) — The batch size per device accelerator core/CPU for training.
  * **per_device_eval_batch_size** (`int`, _optional_ , defaults to 8) — The batch size per device accelerator core/CPU for evaluation.
  * **gradient_accumulation_steps** (`int`, _optional_ , defaults to 1) — Number of updates steps to accumulate the gradients for, before performing a backward/update pass. 
  * **eval_accumulation_steps** (`int`, _optional_) — Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If left unset, the whole predictions are accumulated on the device accelerator before being moved to the CPU (faster but requires more memory).
  * **eval_delay** (`float`, _optional_) — Number of epochs or steps to wait for before the first evaluation can be performed, depending on the eval_strategy.
  * **torch_empty_cache_steps** (`int`, _optional_) — Number of steps to wait before calling `torch.<device>.empty_cache()`. If left unset or set to None, cache will not be emptied. 
  * **learning_rate** (`float`, _optional_ , defaults to 5e-5) — The initial learning rate for `AdamW` optimizer.
  * **weight_decay** (`float`, _optional_ , defaults to 0) — The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in `AdamW` optimizer.
  * **adam_beta1** (`float`, _optional_ , defaults to 0.9) — The beta1 hyperparameter for the `AdamW` optimizer.
  * **adam_beta2** (`float`, _optional_ , defaults to 0.999) — The beta2 hyperparameter for the `AdamW` optimizer.
  * **adam_epsilon** (`float`, _optional_ , defaults to 1e-8) — The epsilon hyperparameter for the `AdamW` optimizer.
  * **max_grad_norm** (`float`, _optional_ , defaults to 1.0) — Maximum gradient norm (for gradient clipping).
  * **num_train_epochs(`float`,** _optional_ , defaults to 3.0) — Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).
  * **max_steps** (`int`, _optional_ , defaults to -1) — If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until `max_steps` is reached.
  * **lr_scheduler_type** (`str` or [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType), _optional_ , defaults to `"linear"`) — The scheduler type to use. See the documentation of [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType) for all possible values.
  * **lr_scheduler_kwargs** (‘dict’, _optional_ , defaults to {}) — The extra arguments for the lr_scheduler. See the documentation of each scheduler for possible values.
  * **warmup_ratio** (`float`, _optional_ , defaults to 0.0) — Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
  * **warmup_steps** (`int`, _optional_ , defaults to 0) — Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.
  * **log_level** (`str`, _optional_ , defaults to `passive`) — Logger log level to use on the main process. Possible choices are the log levels as strings: ‘debug’, ‘info’, ‘warning’, ‘error’ and ‘critical’, plus a ‘passive’ level which doesn’t set anything and keeps the current log level for the Transformers library (which will be `"warning"` by default).
  * **log_level_replica** (`str`, _optional_ , defaults to `"warning"`) — Logger log level to use on replicas. Same choices as `log_level`”
  * **log_on_each_node** (`bool`, _optional_ , defaults to `True`) — In multinode distributed training, whether to log using `log_level` once per node, or only on the main node.
  * **logging_dir** (`str`, _optional_) — [TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.
  * **logging_strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"steps"`) — The logging strategy to adopt during training. Possible values are: 
    * `"no"`: No logging is done during training.
    * `"epoch"`: Logging is done at the end of each epoch.
    * `"steps"`: Logging is done every `logging_steps`.
  * **logging_first_step** (`bool`, _optional_ , defaults to `False`) — Whether to log the first `global_step` or not.
  * **logging_steps** (`int` or `float`, _optional_ , defaults to 500) — Number of update steps between two logs if `logging_strategy="steps"`. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **logging_nan_inf_filter** (`bool`, _optional_ , defaults to `True`) — Whether to filter `nan` and `inf` losses for logging. If set to `True` the loss of every step that is `nan` or `inf` is filtered and the average loss of the current logging window is taken instead. 
  * **save_strategy** (`str` or `SaveStrategy`, _optional_ , defaults to `"steps"`) — The checkpoint save strategy to adopt during training. Possible values are: 
    * `"no"`: No save is done during training.
    * `"epoch"`: Save is done at the end of each epoch.
    * `"steps"`: Save is done every `save_steps`.
    * `"best"`: Save is done whenever a new `best_metric` is achieved.

If `"epoch"` or `"steps"` is chosen, saving will also be performed at the very end of training, always.

  * **save_steps** (`int` or `float`, _optional_ , defaults to 500) — Number of updates steps before two checkpoint saves if `save_strategy="steps"`. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **save_total_limit** (`int`, _optional_) — If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in `output_dir`. When `load_best_model_at_end` is enabled, the “best” checkpoint according to `metric_for_best_model` will always be retained in addition to the most recent ones. For example, for `save_total_limit=5` and `load_best_model_at_end`, the four last checkpoints will always be retained alongside the best model. When `save_total_limit=1` and `load_best_model_at_end`, it is possible that two checkpoints are saved: the last one and the best one (if they are different).
  * **save_safetensors** (`bool`, _optional_ , defaults to `True`) — Use [safetensors](https://huggingface.co/docs/safetensors) saving and loading for state dicts instead of default `torch.load` and `torch.save`.
  * **save_on_each_node** (`bool`, _optional_ , defaults to `False`) — When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one. 

This should not be activated when the different nodes use the same storage as the files will be saved with the same names for each node.

  * **save_only_model** (`bool`, _optional_ , defaults to `False`) — When checkpointing, whether to only save the model, or also the optimizer, scheduler & rng state. Note that when this is true, you won’t be able to resume training from checkpoint. This enables you to save storage by not storing the optimizer, scheduler & rng state. You can only load the model using `from_pretrained` with this option set to `True`.
  * **restore_callback_states_from_checkpoint** (`bool`, _optional_ , defaults to `False`) — Whether to restore the callback states from the checkpoint. If `True`, will override callbacks passed to the `Trainer` if they exist in the checkpoint.”
  * **use_cpu** (`bool`, _optional_ , defaults to `False`) — Whether or not to use cpu. If set to False, we will use cuda or mps device if available.
  * **seed** (`int`, _optional_ , defaults to 42) — Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the `~Trainer.model_init` function to instantiate the model if it has some randomly initialized parameters.
  * **data_seed** (`int`, _optional_) — Random seed to be used with data samplers. If not set, random generators for data sampling will use the same seed as `seed`. This can be used to ensure reproducibility of data sampling, independent of the model seed.
  * **jit_mode_eval** (`bool`, _optional_ , defaults to `False`) — Whether or not to use PyTorch jit trace for inference.
  * **use_ipex** (`bool`, _optional_ , defaults to `False`) — Use Intel extension for PyTorch when it is available. [IPEX installation](https://github.com/intel/intel-extension-for-pytorch).
  * **bf16** (`bool`, _optional_ , defaults to `False`) — Whether to use bf16 16-bit (mixed) precision training instead of 32-bit training. Requires Ampere or higher NVIDIA architecture or Intel XPU or using CPU (use_cpu) or Ascend NPU. This is an experimental API and it may change.
  * **fp16** (`bool`, _optional_ , defaults to `False`) — Whether to use fp16 16-bit (mixed) precision training instead of 32-bit training.
  * **fp16_opt_level** (`str`, _optional_ , defaults to ‘O1’) — For `fp16` training, Apex AMP optimization level selected in [‘O0’, ‘O1’, ‘O2’, and ‘O3’]. See details on the [Apex documentation](https://nvidia.github.io/apex/amp).
  * **fp16_backend** (`str`, _optional_ , defaults to `"auto"`) — This argument is deprecated. Use `half_precision_backend` instead.
  * **half_precision_backend** (`str`, _optional_ , defaults to `"auto"`) — The backend to use for mixed precision training. Must be one of `"auto", "apex", "cpu_amp"`. `"auto"` will use CPU/CUDA AMP or APEX depending on the PyTorch version detected, while the other choices will force the requested backend.
  * **bf16_full_eval** (`bool`, _optional_ , defaults to `False`) — Whether to use full bfloat16 evaluation instead of 32-bit. This will be faster and save memory but can harm metric values. This is an experimental API and it may change.
  * **fp16_full_eval** (`bool`, _optional_ , defaults to `False`) — Whether to use full float16 evaluation instead of 32-bit. This will be faster and save memory but can harm metric values.
  * **tf32** (`bool`, _optional_) — Whether to enable the TF32 mode, available in Ampere and newer GPU architectures. The default value depends on PyTorch’s version default of `torch.backends.cuda.matmul.allow_tf32`. For more details please refer to the [TF32](https://huggingface.co/docs/transformers/perf_train_gpu_one#tf32) documentation. This is an experimental API and it may change.
  * **local_rank** (`int`, _optional_ , defaults to -1) — Rank of the process during distributed training.
  * **ddp_backend** (`str`, _optional_) — The backend to use for distributed training. Must be one of `"nccl"`, `"mpi"`, `"ccl"`, `"gloo"`, `"hccl"`.
  * **tpu_num_cores** (`int`, _optional_) — When training on TPU, the number of TPU cores (automatically passed by launcher script).
  * **dataloader_drop_last** (`bool`, _optional_ , defaults to `False`) — Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size) or not.
  * **eval_steps** (`int` or `float`, _optional_) — Number of update steps between two evaluations if `eval_strategy="steps"`. Will default to the same value as `logging_steps` if not set. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **dataloader_num_workers** (`int`, _optional_ , defaults to 0) — Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the main process.
  * **past_index** (`int`, _optional_ , defaults to -1) — Some models like [TransformerXL](../model_doc/transformerxl) or [XLNet](../model_doc/xlnet) can make use of the past hidden states for their predictions. If this argument is set to a positive int, the `Trainer` will use the corresponding output (usually index 2) as the past state and feed it to the model at the next training step under the keyword argument `mems`.
  * **run_name** (`str`, _optional_ , defaults to `output_dir`) — A descriptor for the run. Typically used for [wandb](https://www.wandb.com/), [mlflow](https://www.mlflow.org/), [comet](https://www.comet.com/site) and [swanlab](https://swanlab.cn) logging. If not specified, will be the same as `output_dir`.
  * **disable_tqdm** (`bool`, _optional_) — Whether or not to disable the tqdm progress bars and table of metrics produced by `~notebook.NotebookTrainingTracker` in Jupyter Notebooks. Will default to `True` if the logging level is set to warn or lower (default), `False` otherwise.
  * **remove_unused_columns** (`bool`, _optional_ , defaults to `True`) — Whether or not to automatically remove the columns unused by the model forward method.
  * **label_names** (`list[str]`, _optional_) — The list of keys in your dictionary of inputs that correspond to the labels. 

Will eventually default to the list of argument names accepted by the model that contain the word “label”, except if the model used is one of the `XxxForQuestionAnswering` in which case it will also include the `["start_positions", "end_positions"]` keys.

  * **load_best_model_at_end** (`bool`, _optional_ , defaults to `False`) — Whether or not to load the best model found during training at the end of training. When this option is enabled, the best checkpoint will always be saved. See [`save_total_limit`](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.save_total_limit) for more. 
  * **metric_for_best_model** (`str`, _optional_) — Use in conjunction with `load_best_model_at_end` to specify the metric to use to compare two different models. Must be the name of a metric returned by the evaluation with or without the prefix `"eval_"`. 

If not specified, this will default to `"loss"` when either `load_best_model_at_end == True` or `lr_scheduler_type == SchedulerType.REDUCE_ON_PLATEAU` (to use the evaluation loss).

If you set this value, `greater_is_better` will default to `True` unless the name ends with “loss”. Don’t forget to set it to `False` if your metric is better when lower.

  * **greater_is_better** (`bool`, _optional_) — Use in conjunction with `load_best_model_at_end` and `metric_for_best_model` to specify if better models should have a greater metric or not. Will default to: 
    * `True` if `metric_for_best_model` is set to a value that doesn’t end in `"loss"`.
    * `False` if `metric_for_best_model` is not set, or set to a value that ends in `"loss"`.
  * **ignore_data_skip** (`bool`, _optional_ , defaults to `False`) — When resuming training, whether or not to skip the epochs and batches to get the data loading at the same stage as in the previous training. If set to `True`, the training will begin faster (as that skipping step can take a long time) but will not yield the same results as the interrupted training would have.
  * **fsdp** (`bool`, `str` or list of `FSDPOption`, _optional_ , defaults to `''`) — Use PyTorch Distributed Parallel Training (in distributed training only). 

A list of options along the following:

    * `"full_shard"`: Shard parameters, gradients and optimizer states.
    * `"shard_grad_op"`: Shard optimizer states and gradients.
    * `"hybrid_shard"`: Apply `FULL_SHARD` within a node, and replicate parameters across nodes.
    * `"hybrid_shard_zero2"`: Apply `SHARD_GRAD_OP` within a node, and replicate parameters across nodes.
    * `"offload"`: Offload parameters and gradients to CPUs (only compatible with `"full_shard"` and `"shard_grad_op"`).
    * `"auto_wrap"`: Automatically recursively wrap layers with FSDP using `default_auto_wrap_policy`.
  * **fsdp_config** (`str` or `dict`, _optional_) — Config to be used with fsdp (Pytorch Distributed Parallel Training). The value is either a location of fsdp json config file (e.g., `fsdp_config.json`) or an already loaded json file as `dict`. 

A List of config and its options:

    * min_num_params (`int`, _optional_ , defaults to `0`): FSDP’s minimum number of parameters for Default Auto Wrapping. (useful only when `fsdp` field is passed).

    * transformer_layer_cls_to_wrap (`list[str]`, _optional_): List of transformer layer class names (case-sensitive) to wrap, e.g, `BertLayer`, `GPTJBlock`, `T5Block` … (useful only when `fsdp` flag is passed).

    * backward_prefetch (`str`, _optional_) FSDP’s backward prefetch mode. Controls when to prefetch next set of parameters (useful only when `fsdp` field is passed).

A list of options along the following:

      * `"backward_pre"` : Prefetches the next set of parameters before the current set of parameter’s gradient computation.
      * `"backward_post"` : This prefetches the next set of parameters after the current set of parameter’s gradient computation.
    * forward_prefetch (`bool`, _optional_ , defaults to `False`) FSDP’s forward prefetch mode (useful only when `fsdp` field is passed). If `"True"`, then FSDP explicitly prefetches the next upcoming all-gather while executing in the forward pass.

    * limit_all_gathers (`bool`, _optional_ , defaults to `False`) FSDP’s limit_all_gathers (useful only when `fsdp` field is passed). If `"True"`, FSDP explicitly synchronizes the CPU thread to prevent too many in-flight all-gathers.

    * use_orig_params (`bool`, _optional_ , defaults to `True`) If `"True"`, allows non-uniform `requires_grad` during init, which means support for interspersed frozen and trainable parameters. Useful in cases such as parameter-efficient fine-tuning. Please refer this [blog](<https://dev-discuss.pytorch.org/t/rethinking-pytorch-fully-sharded-data-parallel-fsdp-from-first-principles/1019>

    * sync_module_states (`bool`, _optional_ , defaults to `True`) If `"True"`, each individually wrapped FSDP unit will broadcast module parameters from rank 0 to ensure they are the same across all ranks after initialization

    * cpu_ram_efficient_loading (`bool`, _optional_ , defaults to `False`) If `"True"`, only the first process loads the pretrained model checkpoint while all other processes have empty weights. When this setting as `"True"`, `sync_module_states` also must to be `"True"`, otherwise all the processes except the main process would have random weights leading to unexpected behaviour during training.

    * activation_checkpointing (`bool`, _optional_ , defaults to `False`): If `"True"`, activation checkpointing is a technique to reduce memory usage by clearing activations of certain layers and recomputing them during a backward pass. Effectively, this trades extra computation time for reduced memory usage.

    * xla (`bool`, _optional_ , defaults to `False`): Whether to use PyTorch/XLA Fully Sharded Data Parallel Training. This is an experimental feature and its API may evolve in the future.

    * xla_fsdp_settings (`dict`, _optional_) The value is a dictionary which stores the XLA FSDP wrapping parameters.

For a complete list of options, please see [here](https://github.com/pytorch/xla/blob/master/torch_xla/distributed/fsdp/xla_fully_sharded_data_parallel.py).

    * xla_fsdp_grad_ckpt (`bool`, _optional_ , defaults to `False`): Will use gradient checkpointing over each nested XLA FSDP wrapped layer. This setting can only be used when the xla flag is set to true, and an auto wrapping policy is specified through fsdp_min_num_params or fsdp_transformer_layer_cls_to_wrap.

  * **deepspeed** (`str` or `dict`, _optional_) — Use [Deepspeed](https://github.com/deepspeedai/DeepSpeed). This is an experimental feature and its API may evolve in the future. The value is either the location of DeepSpeed json config file (e.g., `ds_config.json`) or an already loaded json file as a `dict`” 
  * **accelerator_config** (`str`, `dict`, or `AcceleratorConfig`, _optional_) — Config to be used with the internal `Accelerator` implementation. The value is either a location of accelerator json config file (e.g., `accelerator_config.json`), an already loaded json file as `dict`, or an instance of `AcceleratorConfig`. 

A list of config and its options:

    * split_batches (`bool`, _optional_ , defaults to `False`): Whether or not the accelerator should split the batches yielded by the dataloaders across the devices. If `True` the actual batch size used will be the same on any kind of distributed processes, but it must be a round multiple of the `num_processes` you are using. If `False`, actual batch size used will be the one set in your script multiplied by the number of processes.
    * dispatch_batches (`bool`, _optional_): If set to `True`, the dataloader prepared by the Accelerator is only iterated through on the main process and then the batches are split and broadcast to each process. Will default to `True` for `DataLoader` whose underlying dataset is an `IterableDataset`, `False` otherwise.
    * even_batches (`bool`, _optional_ , defaults to `True`): If set to `True`, in cases where the total batch size across all processes does not exactly divide the dataset, samples at the start of the dataset will be duplicated so the batch can be divided equally among all workers.
    * use_seedable_sampler (`bool`, _optional_ , defaults to `True`): Whether or not use a fully seedable random sampler (`accelerate.data_loader.SeedableRandomSampler`). Ensures training results are fully reproducible using a different sampling technique. While seed-to-seed results may differ, on average the differences are negligible when using multiple different seeds to compare. Should also be ran with `~utils.set_seed` for the best results.
    * use_configured_state (`bool`, _optional_ , defaults to `False`): Whether or not to use a pre-configured `AcceleratorState` or `PartialState` defined before calling `TrainingArguments`. If `True`, an `Accelerator` or `PartialState` must be initialized. Note that by doing so, this could lead to issues with hyperparameter tuning.
  * **label_smoothing_factor** (`float`, _optional_ , defaults to 0.0) — The label smoothing factor to use. Zero means no label smoothing, otherwise the underlying onehot-encoded labels are changed from 0s and 1s to `label_smoothing_factor/num_labels` and `1 - label_smoothing_factor + label_smoothing_factor/num_labels` respectively.
  * **debug** (`str` or list of `DebugOption`, _optional_ , defaults to `""`) — Enable one or more debug features. This is an experimental feature. 

Possible options are:

    * `"underflow_overflow"`: detects overflow in model’s input/outputs and reports the last frames that led to the event
    * `"tpu_metrics_debug"`: print debug metrics on TPU

The options should be separated by whitespaces.

  * **optim** (`str` or `training_args.OptimizerNames`, _optional_ , defaults to `"adamw_torch"`) — The optimizer to use, such as “adamw_torch”, “adamw_torch_fused”, “adamw_apex_fused”, “adamw_anyprecision”, “adafactor”. See `OptimizerNames` in [training_args.py](https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py) for a full list of optimizers.
  * **optim_args** (`str`, _optional_) — Optional arguments that are supplied to optimizers such as AnyPrecisionAdamW, AdEMAMix, and GaLore.
  * **group_by_length** (`bool`, _optional_ , defaults to `False`) — Whether or not to group together samples of roughly the same length in the training dataset (to minimize padding applied and be more efficient). Only useful if applying dynamic padding.
  * **length_column_name** (`str`, _optional_ , defaults to `"length"`) — Column name for precomputed lengths. If the column exists, grouping by length will use these values rather than computing them on train startup. Ignored unless `group_by_length` is `True` and the dataset is an instance of `Dataset`.
  * **report_to** (`str` or `list[str]`, _optional_ , defaults to `"all"`) — The list of integrations to report the results and logs to. Supported platforms are `"azure_ml"`, `"clearml"`, `"codecarbon"`, `"comet_ml"`, `"dagshub"`, `"dvclive"`, `"flyte"`, `"mlflow"`, `"neptune"`, `"swanlab"`, `"tensorboard"`, and `"wandb"`. Use `"all"` to report to all integrations installed, `"none"` for no integrations.
  * **ddp_find_unused_parameters** (`bool`, _optional_) — When using distributed training, the value of the flag `find_unused_parameters` passed to `DistributedDataParallel`. Will default to `False` if gradient checkpointing is used, `True` otherwise.
  * **ddp_bucket_cap_mb** (`int`, _optional_) — When using distributed training, the value of the flag `bucket_cap_mb` passed to `DistributedDataParallel`.
  * **ddp_broadcast_buffers** (`bool`, _optional_) — When using distributed training, the value of the flag `broadcast_buffers` passed to `DistributedDataParallel`. Will default to `False` if gradient checkpointing is used, `True` otherwise.
  * **dataloader_pin_memory** (`bool`, _optional_ , defaults to `True`) — Whether you want to pin memory in data loaders or not. Will default to `True`.
  * **dataloader_persistent_workers** (`bool`, _optional_ , defaults to `False`) — If True, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. Can potentially speed up training, but will increase RAM usage. Will default to `False`.
  * **dataloader_prefetch_factor** (`int`, _optional_) — Number of batches loaded in advance by each worker. 2 means there will be a total of 2 * num_workers batches prefetched across all workers.
  * **skip_memory_metrics** (`bool`, _optional_ , defaults to `True`) — Whether to skip adding of memory profiler reports to metrics. This is skipped by default because it slows down the training and evaluation speed.
  * **push_to_hub** (`bool`, _optional_ , defaults to `False`) — Whether or not to push the model to the Hub every time the model is saved. If this is activated, `output_dir` will begin a git directory synced with the repo (determined by `hub_model_id`) and the content will be pushed each time a save is triggered (depending on your `save_strategy`). Calling [save_model()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.save_model) will also trigger a push. 
  * **resume_from_checkpoint** (`str`, _optional_) — The path to a folder with a valid checkpoint for your model. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **hub_model_id** (`str`, _optional_) — The name of the repository to keep in sync with the local _output_dir_. It can be a simple model ID in which case the model will be pushed in your namespace. Otherwise it should be the whole repository name, for instance `"user_name/model"`, which allows you to push to an organization you are a member of with `"organization_name/model"`. Will default to `user_name/output_dir_name` with _output_dir_name_ being the name of `output_dir`. 

Will default to the name of `output_dir`.

  * **hub_strategy** (`str` or `HubStrategy`, _optional_ , defaults to `"every_save"`) — Defines the scope of what is pushed to the Hub and when. Possible values are: 
    * `"end"`: push the model, its configuration, the processing class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card when the [save_model()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.save_model) method is called.
    * `"every_save"`: push the model, its configuration, the processing class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card each time there is a model save. The pushes are asynchronous to not block training, and in case the save are very frequent, a new push is only attempted if the previous one is finished. A last push is made with the final model at the end of training.
    * `"checkpoint"`: like `"every_save"` but the latest checkpoint is also pushed in a subfolder named last-checkpoint, allowing you to resume training easily with `trainer.train(resume_from_checkpoint="last-checkpoint")`.
    * `"all_checkpoints"`: like `"checkpoint"` but all checkpoints are pushed like they appear in the output folder (so you will get one checkpoint folder per folder in your final repository)
  * **hub_token** (`str`, _optional_) — The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with `huggingface-cli login`.
  * **hub_private_repo** (`bool`, _optional_) — Whether to make the repo private. If `None` (default), the repo will be public unless the organization’s default is private. This value is ignored if the repo already exists.
  * **hub_always_push** (`bool`, _optional_ , defaults to `False`) — Unless this is `True`, the `Trainer` will skip pushing a checkpoint when the previous push is not finished.
  * **hub_revision** (`str`, _optional_) — The revision to use when pushing to the Hub. Can be a branch name, a tag, or a commit hash.
  * **gradient_checkpointing** (`bool`, _optional_ , defaults to `False`) — If True, use gradient checkpointing to save memory at the expense of slower backward pass.
  * **gradient_checkpointing_kwargs** (`dict`, _optional_ , defaults to `None`) — Key word arguments to be passed to the `gradient_checkpointing_enable` method.
  * **include_inputs_for_metrics** (`bool`, _optional_ , defaults to `False`) — This argument is deprecated. Use `include_for_metrics` instead, e.g, `include_for_metrics = ["inputs"]`.
  * **include_for_metrics** (`list[str]`, _optional_ , defaults to `[]`) — Include additional data in the `compute_metrics` function if needed for metrics computation. Possible options to add to `include_for_metrics` list: 
    * `"inputs"`: Input data passed to the model, intended for calculating input dependent metrics.
    * `"loss"`: Loss values computed during evaluation, intended for calculating loss dependent metrics.
  * **eval_do_concat_batches** (`bool`, _optional_ , defaults to `True`) — Whether to recursively concat inputs/losses/labels/predictions across batches. If `False`, will instead store them as lists, with each batch kept separate.
  * **auto_find_batch_size** (`bool`, _optional_ , defaults to `False`) — Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding CUDA Out-of-Memory errors. Requires accelerate to be installed (`pip install accelerate`)
  * **full_determinism** (`bool`, _optional_ , defaults to `False`) — If `True`, [enable_full_determinism()](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.enable_full_determinism) is called instead of [set_seed()](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.set_seed) to ensure reproducible results in distributed training. Important: this will negatively impact the performance, so only use it for debugging.
  * **torchdynamo** (`str`, _optional_) — If set, the backend compiler for TorchDynamo. Possible choices are `"eager"`, `"aot_eager"`, `"inductor"`, `"nvfuser"`, `"aot_nvfuser"`, `"aot_cudagraphs"`, `"ofi"`, `"fx2trt"`, `"onnxrt"` and `"ipex"`.
  * **ray_scope** (`str`, _optional_ , defaults to `"last"`) — The scope to use when doing hyperparameter search with Ray. By default, `"last"` will be used. Ray will then use the last checkpoint of all trials, compare those, and select the best one. However, other options are also available. See the [Ray documentation](https://docs.ray.io/en/latest/tune/api_docs/analysis.html#ray.tune.ExperimentAnalysis.get_best_trial) for more options.
  * **ddp_timeout** (`int`, _optional_ , defaults to 1800) — The timeout for `torch.distributed.init_process_group` calls, used to avoid GPU socket timeouts when performing slow operations in distributed runnings. Please refer the [PyTorch documentation] (<https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group>) for more information.
  * **use_mps_device** (`bool`, _optional_ , defaults to `False`) — This argument is deprecated.`mps` device will be used if it is available similar to `cuda` device.
  * **torch_compile** (`bool`, _optional_ , defaults to `False`) — Whether or not to compile the model using PyTorch 2.0 [`torch.compile`](https://pytorch.org/get-started/pytorch-2.0/). 

This will use the best defaults for the [`torch.compile` API](https://pytorch.org/docs/stable/generated/torch.compile.html?highlight=torch+compile#torch.compile). You can customize the defaults with the argument `torch_compile_backend` and `torch_compile_mode` but we don’t guarantee any of them will work as the support is progressively rolled in in PyTorch.

This flag and the whole compile API is experimental and subject to change in future releases.

  * **torch_compile_backend** (`str`, _optional_) — The backend to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`. 

Refer to the PyTorch doc for possible values and note that they may change across PyTorch versions.

This flag is experimental and subject to change in future releases.

  * **torch_compile_mode** (`str`, _optional_) — The mode to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`. 

Refer to the PyTorch doc for possible values and note that they may change across PyTorch versions.

This flag is experimental and subject to change in future releases.

  * **include_tokens_per_second** (`bool`, _optional_) — Whether or not to compute the number of tokens per second per device for training speed metrics. 

This will iterate over the entire training dataloader once beforehand,

and will slow down the entire process.

  * **include_num_input_tokens_seen** (`bool`, _optional_) — Whether or not to track the number of input tokens seen throughout training. 

May be slower in distributed training as gather operations must be called.

  * **neftune_noise_alpha** (`Optional[float]`) — If not `None`, this will activate NEFTune noise embeddings. This can drastically improve model performance for instruction fine-tuning. Check out the [original paper](https://huggingface.co/papers/2310.05914) and the [original code](https://github.com/neelsjain/NEFTune). Support transformers `PreTrainedModel` and also `PeftModel` from peft. The original paper used values in the range [5.0, 15.0].
  * **optim_target_modules** (`Union[str, list[str]]`, _optional_) — The target modules to optimize, i.e. the module names that you would like to train. Currently used for the GaLore algorithm (<https://huggingface.co/papers/2403.03507>) and APOLLO algorithm (<https://huggingface.co/papers/2412.05270>). See GaLore implementation (<https://github.com/jiaweizzhao/GaLore>) and APOLLO implementation (<https://github.com/zhuhanqing/APOLLO>) for more details. You need to make sure to pass a valid GaLore or APOLLO optimizer, e.g., one of: “apollo_adamw”, “galore_adamw”, “galore_adamw_8bit”, “galore_adafactor” and make sure that the target modules are `nn.Linear` modules only.
  * **batch_eval_metrics** (`Optional[bool]`, defaults to `False`) — If set to `True`, evaluation will call compute_metrics at the end of each batch to accumulate statistics rather than saving all eval logits in memory. When set to `True`, you must pass a compute_metrics function that takes a boolean argument `compute_result`, which when passed `True`, will trigger the final global summary statistics from the batch-level summary statistics you’ve accumulated over the evaluation set.
  * **eval_on_start** (`bool`, _optional_ , defaults to `False`) — Whether to perform a evaluation step (sanity check) before the training to ensure the validation steps works correctly.
  * **eval_use_gather_object** (`bool`, _optional_ , defaults to `False`) — Whether to run recursively gather object in a nested list/tuple/dictionary of objects from all devices. This should only be enabled if users are not just returning tensors, and this is actively discouraged by PyTorch.
  * **use_liger_kernel** (`bool`, _optional_ , defaults to `False`) — Whether enable [Liger](https://github.com/linkedin/Liger-Kernel) Kernel for LLM model training. It can effectively increase multi-GPU training throughput by ~20% and reduces memory usage by ~60%, works out of the box with flash attention, PyTorch FSDP, and Microsoft DeepSpeed. Currently, it supports llama, mistral, mixtral and gemma models.
  * **liger_kernel_config** (`Optional[dict]`, _optional_) — Configuration to be used for Liger Kernel. When use_liger_kernel=True, this dict is passed as keyword arguments to the `_apply_liger_kernel_to_instance` function, which specifies which kernels to apply. Available options vary by model but typically include: ‘rope’, ‘swiglu’, ‘cross_entropy’, ‘fused_linear_cross_entropy’, ‘rms_norm’, etc. If `None`, use the default kernel configurations.
  * **average_tokens_across_devices** (`bool`, _optional_ , defaults to `False`) — Whether or not to average tokens across devices. If enabled, will use all_reduce to synchronize num_tokens_in_batch for precise loss calculation. Reference: <https://github.com/huggingface/transformers/issues/34242>

TrainingArguments is the subset of the arguments we use in our example scripts **which relate to the training loop itself**.

Using [HfArgumentParser](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the command line.

Returns the log level to be used depending on whether this process is the main process of node 0, main process of node non-0, or a non-main process.

For the main process the log level defaults to the logging level set (`logging.WARNING` if you didn’t do anything) unless overridden by `log_level` argument.

For the replica processes the log level defaults to `logging.WARNING` unless overridden by `log_level_replica` argument.

The choice between the main and replica process settings is made according to the return value of `should_log`.

Get number of steps used for a linear warmup.

Parameters 

  * **local** (`bool`, _optional_ , defaults to `True`) — if `True` first means process of rank 0 of each node if `False` first means process of rank 0 of node rank 0 In multi-node environment with a shared filesystem you most likely will want to use `local=False` so that only the main process of the first node will do the processing. If however, the filesystem is not shared, then the main process of each node will need to do the processing, which is the default behavior.
  * **desc** (`str`, _optional_ , defaults to `"work"`) — a work description to be used in debug logs

A context manager for torch distributed environment where on needs to do something on the main process, while blocking replicas, and when it’s finished releasing the replicas.

One such use is for `datasets`’s `map` feature which to be efficient should be run once on the main process, which upon completion saves a cached version of results and which then automatically gets loaded by the replicas.

Parameters 

  * **drop_last** (`bool`, _optional_ , defaults to `False`) — Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size) or not.
  * **num_workers** (`int`, _optional_ , defaults to 0) — Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the main process.
  * **pin_memory** (`bool`, _optional_ , defaults to `True`) — Whether you want to pin memory in data loaders or not. Will default to `True`.
  * **persistent_workers** (`bool`, _optional_ , defaults to `False`) — If True, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. Can potentially speed up training, but will increase RAM usage. Will default to `False`.
  * **prefetch_factor** (`int`, _optional_) — Number of batches loaded in advance by each worker. 2 means there will be a total of 2 * num_workers batches prefetched across all workers.
  * **auto_find_batch_size** (`bool`, _optional_ , defaults to `False`) — Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding CUDA Out-of-Memory errors. Requires accelerate to be installed (`pip install accelerate`)
  * **ignore_data_skip** (`bool`, _optional_ , defaults to `False`) — When resuming training, whether or not to skip the epochs and batches to get the data loading at the same stage as in the previous training. If set to `True`, the training will begin faster (as that skipping step can take a long time) but will not yield the same results as the interrupted training would have.
  * **sampler_seed** (`int`, _optional_) — Random seed to be used with data samplers. If not set, random generators for data sampling will use the same seed as `self.seed`. This can be used to ensure reproducibility of data sampling, independent of the model seed.

A method that regroups all arguments linked to the dataloaders creation.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_dataloader(train_batch_size=16, eval_batch_size=64)
    >>> args.per_device_train_batch_size
    16

Parameters 

  * **strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"no"`) — The evaluation strategy to adopt during training. Possible values are: 
    * `"no"`: No evaluation is done during training.
    * `"steps"`: Evaluation is done (and logged) every `steps`.
    * `"epoch"`: Evaluation is done at the end of each epoch.

Setting a `strategy` different from `"no"` will set `self.do_eval` to `True`.

  * **steps** (`int`, _optional_ , defaults to 500) — Number of update steps between two evaluations if `strategy="steps"`.
  * **batch_size** (`int` _optional_ , defaults to 8) — The batch size per device (GPU/TPU core/CPU…) used for evaluation.
  * **accumulation_steps** (`int`, _optional_) — Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If left unset, the whole predictions are accumulated on GPU/TPU before being moved to the CPU (faster but requires more memory).
  * **delay** (`float`, _optional_) — Number of epochs or steps to wait for before the first evaluation can be performed, depending on the eval_strategy.
  * **loss_only** (`bool`, _optional_ , defaults to `False`) — Ignores all outputs except the loss.
  * **jit_mode** (`bool`, _optional_) — Whether or not to use PyTorch jit trace for inference.

A method that regroups all arguments linked to evaluation.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_evaluate(strategy="steps", steps=100)
    >>> args.eval_steps
    100

Parameters 

  * **strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"steps"`) — The logging strategy to adopt during training. Possible values are: 
    * `"no"`: No logging is done during training.
    * `"epoch"`: Logging is done at the end of each epoch.
    * `"steps"`: Logging is done every `logging_steps`.
  * **steps** (`int`, _optional_ , defaults to 500) — Number of update steps between two logs if `strategy="steps"`.
  * **level** (`str`, _optional_ , defaults to `"passive"`) — Logger log level to use on the main process. Possible choices are the log levels as strings: `"debug"`, `"info"`, `"warning"`, `"error"` and `"critical"`, plus a `"passive"` level which doesn’t set anything and lets the application set the level.
  * **report_to** (`str` or `list[str]`, _optional_ , defaults to `"all"`) — The list of integrations to report the results and logs to. Supported platforms are `"azure_ml"`, `"clearml"`, `"codecarbon"`, `"comet_ml"`, `"dagshub"`, `"dvclive"`, `"flyte"`, `"mlflow"`, `"neptune"`, `"swanlab"`, `"tensorboard"`, and `"wandb"`. Use `"all"` to report to all integrations installed, `"none"` for no integrations.
  * **first_step** (`bool`, _optional_ , defaults to `False`) — Whether to log and evaluate the first `global_step` or not.
  * **nan_inf_filter** (`bool`, _optional_ , defaults to `True`) — Whether to filter `nan` and `inf` losses for logging. If set to `True` the loss of every step that is `nan` or `inf` is filtered and the average loss of the current logging window is taken instead. 
  * **on_each_node** (`bool`, _optional_ , defaults to `True`) — In multinode distributed training, whether to log using `log_level` once per node, or only on the main node.
  * **replica_level** (`str`, _optional_ , defaults to `"passive"`) — Logger log level to use on replicas. Same choices as `log_level`

A method that regroups all arguments linked to logging.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_logging(strategy="steps", steps=100)
    >>> args.logging_steps
    100

Parameters 

  * **name** (`str` or [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType), _optional_ , defaults to `"linear"`) — The scheduler type to use. See the documentation of [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType) for all possible values.
  * **num_epochs(`float`,** _optional_ , defaults to 3.0) — Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).
  * **max_steps** (`int`, _optional_ , defaults to -1) — If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until `max_steps` is reached.
  * **warmup_ratio** (`float`, _optional_ , defaults to 0.0) — Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
  * **warmup_steps** (`int`, _optional_ , defaults to 0) — Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.

A method that regroups all arguments linked to the learning rate scheduler and its hyperparameters.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_lr_scheduler(name="cosine", warmup_ratio=0.05)
    >>> args.warmup_ratio
    0.05

Parameters 

  * **name** (`str` or `training_args.OptimizerNames`, _optional_ , defaults to `"adamw_torch"`) — The optimizer to use: `"adamw_torch"`, `"adamw_torch_fused"`, `"adamw_apex_fused"`, `"adamw_anyprecision"` or `"adafactor"`.
  * **learning_rate** (`float`, _optional_ , defaults to 5e-5) — The initial learning rate.
  * **weight_decay** (`float`, _optional_ , defaults to 0) — The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights.
  * **beta1** (`float`, _optional_ , defaults to 0.9) — The beta1 hyperparameter for the adam optimizer or its variants.
  * **beta2** (`float`, _optional_ , defaults to 0.999) — The beta2 hyperparameter for the adam optimizer or its variants.
  * **epsilon** (`float`, _optional_ , defaults to 1e-8) — The epsilon hyperparameter for the adam optimizer or its variants.
  * **args** (`str`, _optional_) — Optional arguments that are supplied to AnyPrecisionAdamW (only useful when `optim="adamw_anyprecision"`).

A method that regroups all arguments linked to the optimizer and its hyperparameters.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_optimizer(name="adamw_torch", beta1=0.8)
    >>> args.optim
    'adamw_torch'

Parameters 

  * **model_id** (`str`) — The name of the repository to keep in sync with the local _output_dir_. It can be a simple model ID in which case the model will be pushed in your namespace. Otherwise it should be the whole repository name, for instance `"user_name/model"`, which allows you to push to an organization you are a member of with `"organization_name/model"`.
  * **strategy** (`str` or `HubStrategy`, _optional_ , defaults to `"every_save"`) — Defines the scope of what is pushed to the Hub and when. Possible values are: 
    * `"end"`: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card when the [save_model()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.save_model) method is called.
    * `"every_save"`: push the model, its configuration, the processing_class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card each time there is a model save. The pushes are asynchronous to not block training, and in case the save are very frequent, a new push is only attempted if the previous one is finished. A last push is made with the final model at the end of training.
    * `"checkpoint"`: like `"every_save"` but the latest checkpoint is also pushed in a subfolder named last-checkpoint, allowing you to resume training easily with `trainer.train(resume_from_checkpoint="last-checkpoint")`.
    * `"all_checkpoints"`: like `"checkpoint"` but all checkpoints are pushed like they appear in the output folder (so you will get one checkpoint folder per folder in your final repository)
  * **token** (`str`, _optional_) — The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with `huggingface-cli login`.
  * **private_repo** (`bool`, _optional_ , defaults to `False`) — Whether to make the repo private. If `None` (default), the repo will be public unless the organization’s default is private. This value is ignored if the repo already exists.
  * **always_push** (`bool`, _optional_ , defaults to `False`) — Unless this is `True`, the `Trainer` will skip pushing a checkpoint when the previous push is not finished.
  * **revision** (`str`, _optional_) — The revision to use when pushing to the Hub. Can be a branch name, a tag, or a commit hash.

A method that regroups all arguments linked to synchronizing checkpoints with the Hub.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_push_to_hub("me/awesome-model")
    >>> args.hub_model_id
    'me/awesome-model'

Parameters 

  * **strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"steps"`) — The checkpoint save strategy to adopt during training. Possible values are: 
    * `"no"`: No save is done during training.
    * `"epoch"`: Save is done at the end of each epoch.
    * `"steps"`: Save is done every `save_steps`.
  * **steps** (`int`, _optional_ , defaults to 500) — Number of updates steps before two checkpoint saves if `strategy="steps"`.
  * **total_limit** (`int`, _optional_) — If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in `output_dir`.
  * **on_each_node** (`bool`, _optional_ , defaults to `False`) — When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one. 

This should not be activated when the different nodes use the same storage as the files will be saved with the same names for each node.

A method that regroups all arguments linked to checkpoint saving.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_save(strategy="steps", steps=100)
    >>> args.save_steps
    100

Parameters 

  * **batch_size** (`int` _optional_ , defaults to 8) — The batch size per device (GPU/TPU core/CPU…) used for testing.
  * **loss_only** (`bool`, _optional_ , defaults to `False`) — Ignores all outputs except the loss.
  * **jit_mode** (`bool`, _optional_) — Whether or not to use PyTorch jit trace for inference.

A method that regroups all basic arguments linked to testing on a held-out dataset.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_testing(batch_size=32)
    >>> args.per_device_eval_batch_size
    32

Parameters 

  * **learning_rate** (`float`, _optional_ , defaults to 5e-5) — The initial learning rate for the optimizer.
  * **batch_size** (`int` _optional_ , defaults to 8) — The batch size per device (GPU/TPU core/CPU…) used for training.
  * **weight_decay** (`float`, _optional_ , defaults to 0) — The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in the optimizer.
  * **num_train_epochs(`float`,** _optional_ , defaults to 3.0) — Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).
  * **max_steps** (`int`, _optional_ , defaults to -1) — If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until `max_steps` is reached.
  * **gradient_accumulation_steps** (`int`, _optional_ , defaults to 1) — Number of updates steps to accumulate the gradients for, before performing a backward/update pass. 
  * **seed** (`int`, _optional_ , defaults to 42) — Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the `~Trainer.model_init` function to instantiate the model if it has some randomly initialized parameters.
  * **gradient_checkpointing** (`bool`, _optional_ , defaults to `False`) — If True, use gradient checkpointing to save memory at the expense of slower backward pass.

A method that regroups all basic arguments linked to the training.

Example:
    
    
    >>> from transformers import TrainingArguments
    
    >>> args = TrainingArguments("working_dir")
    >>> args = args.set_training(learning_rate=1e-4, batch_size=32)
    >>> args.learning_rate
    1e-4

Serializes this instance while replace `Enum` by their values (for JSON serialization support). It obfuscates the token values by removing their value.

Serializes this instance to a JSON string.

Sanitized serialization to use with TensorBoard’s hparams

##  Seq2SeqTrainingArguments

Parameters 

  * **output_dir** (`str`, _optional_ , defaults to `"trainer_output"`) — The output directory where the model predictions and checkpoints will be written.
  * **overwrite_output_dir** (`bool`, _optional_ , defaults to `False`) — If `True`, overwrite the content of the output directory. Use this to continue training if `output_dir` points to a checkpoint directory.
  * **do_train** (`bool`, _optional_ , defaults to `False`) — Whether to run training or not. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **do_eval** (`bool`, _optional_) — Whether to run evaluation on the validation set or not. Will be set to `True` if `eval_strategy` is different from `"no"`. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **do_predict** (`bool`, _optional_ , defaults to `False`) — Whether to run predictions on the test set or not. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **eval_strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"no"`) — The evaluation strategy to adopt during training. Possible values are: 
    * `"no"`: No evaluation is done during training.
    * `"steps"`: Evaluation is done (and logged) every `eval_steps`.
    * `"epoch"`: Evaluation is done at the end of each epoch.
  * **prediction_loss_only** (`bool`, _optional_ , defaults to `False`) — When performing evaluation and generating predictions, only returns the loss.
  * **per_device_train_batch_size** (`int`, _optional_ , defaults to 8) — The batch size per device accelerator core/CPU for training.
  * **per_device_eval_batch_size** (`int`, _optional_ , defaults to 8) — The batch size per device accelerator core/CPU for evaluation.
  * **gradient_accumulation_steps** (`int`, _optional_ , defaults to 1) — Number of updates steps to accumulate the gradients for, before performing a backward/update pass. 
  * **eval_accumulation_steps** (`int`, _optional_) — Number of predictions steps to accumulate the output tensors for, before moving the results to the CPU. If left unset, the whole predictions are accumulated on the device accelerator before being moved to the CPU (faster but requires more memory).
  * **eval_delay** (`float`, _optional_) — Number of epochs or steps to wait for before the first evaluation can be performed, depending on the eval_strategy.
  * **torch_empty_cache_steps** (`int`, _optional_) — Number of steps to wait before calling `torch.<device>.empty_cache()`. If left unset or set to None, cache will not be emptied. 
  * **learning_rate** (`float`, _optional_ , defaults to 5e-5) — The initial learning rate for `AdamW` optimizer.
  * **weight_decay** (`float`, _optional_ , defaults to 0) — The weight decay to apply (if not zero) to all layers except all bias and LayerNorm weights in `AdamW` optimizer.
  * **adam_beta1** (`float`, _optional_ , defaults to 0.9) — The beta1 hyperparameter for the `AdamW` optimizer.
  * **adam_beta2** (`float`, _optional_ , defaults to 0.999) — The beta2 hyperparameter for the `AdamW` optimizer.
  * **adam_epsilon** (`float`, _optional_ , defaults to 1e-8) — The epsilon hyperparameter for the `AdamW` optimizer.
  * **max_grad_norm** (`float`, _optional_ , defaults to 1.0) — Maximum gradient norm (for gradient clipping).
  * **num_train_epochs(`float`,** _optional_ , defaults to 3.0) — Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).
  * **max_steps** (`int`, _optional_ , defaults to -1) — If set to a positive number, the total number of training steps to perform. Overrides `num_train_epochs`. For a finite dataset, training is reiterated through the dataset (if all data is exhausted) until `max_steps` is reached.
  * **lr_scheduler_type** (`str` or [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType), _optional_ , defaults to `"linear"`) — The scheduler type to use. See the documentation of [SchedulerType](/docs/transformers/v4.53.1/en/main_classes/optimizer_schedules#transformers.SchedulerType) for all possible values.
  * **lr_scheduler_kwargs** (‘dict’, _optional_ , defaults to {}) — The extra arguments for the lr_scheduler. See the documentation of each scheduler for possible values.
  * **warmup_ratio** (`float`, _optional_ , defaults to 0.0) — Ratio of total training steps used for a linear warmup from 0 to `learning_rate`.
  * **warmup_steps** (`int`, _optional_ , defaults to 0) — Number of steps used for a linear warmup from 0 to `learning_rate`. Overrides any effect of `warmup_ratio`.
  * **log_level** (`str`, _optional_ , defaults to `passive`) — Logger log level to use on the main process. Possible choices are the log levels as strings: ‘debug’, ‘info’, ‘warning’, ‘error’ and ‘critical’, plus a ‘passive’ level which doesn’t set anything and keeps the current log level for the Transformers library (which will be `"warning"` by default).
  * **log_level_replica** (`str`, _optional_ , defaults to `"warning"`) — Logger log level to use on replicas. Same choices as `log_level`”
  * **log_on_each_node** (`bool`, _optional_ , defaults to `True`) — In multinode distributed training, whether to log using `log_level` once per node, or only on the main node.
  * **logging_dir** (`str`, _optional_) — [TensorBoard](https://www.tensorflow.org/tensorboard) log directory. Will default to *output_dir/runs/**CURRENT_DATETIME_HOSTNAME***.
  * **logging_strategy** (`str` or [IntervalStrategy](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.IntervalStrategy), _optional_ , defaults to `"steps"`) — The logging strategy to adopt during training. Possible values are: 
    * `"no"`: No logging is done during training.
    * `"epoch"`: Logging is done at the end of each epoch.
    * `"steps"`: Logging is done every `logging_steps`.
  * **logging_first_step** (`bool`, _optional_ , defaults to `False`) — Whether to log the first `global_step` or not.
  * **logging_steps** (`int` or `float`, _optional_ , defaults to 500) — Number of update steps between two logs if `logging_strategy="steps"`. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **logging_nan_inf_filter** (`bool`, _optional_ , defaults to `True`) — Whether to filter `nan` and `inf` losses for logging. If set to `True` the loss of every step that is `nan` or `inf` is filtered and the average loss of the current logging window is taken instead. 
  * **save_strategy** (`str` or `SaveStrategy`, _optional_ , defaults to `"steps"`) — The checkpoint save strategy to adopt during training. Possible values are: 
    * `"no"`: No save is done during training.
    * `"epoch"`: Save is done at the end of each epoch.
    * `"steps"`: Save is done every `save_steps`.
    * `"best"`: Save is done whenever a new `best_metric` is achieved.

If `"epoch"` or `"steps"` is chosen, saving will also be performed at the very end of training, always.

  * **save_steps** (`int` or `float`, _optional_ , defaults to 500) — Number of updates steps before two checkpoint saves if `save_strategy="steps"`. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **save_total_limit** (`int`, _optional_) — If a value is passed, will limit the total amount of checkpoints. Deletes the older checkpoints in `output_dir`. When `load_best_model_at_end` is enabled, the “best” checkpoint according to `metric_for_best_model` will always be retained in addition to the most recent ones. For example, for `save_total_limit=5` and `load_best_model_at_end`, the four last checkpoints will always be retained alongside the best model. When `save_total_limit=1` and `load_best_model_at_end`, it is possible that two checkpoints are saved: the last one and the best one (if they are different).
  * **save_safetensors** (`bool`, _optional_ , defaults to `True`) — Use [safetensors](https://huggingface.co/docs/safetensors) saving and loading for state dicts instead of default `torch.load` and `torch.save`.
  * **save_on_each_node** (`bool`, _optional_ , defaults to `False`) — When doing multi-node distributed training, whether to save models and checkpoints on each node, or only on the main one. 

This should not be activated when the different nodes use the same storage as the files will be saved with the same names for each node.

  * **save_only_model** (`bool`, _optional_ , defaults to `False`) — When checkpointing, whether to only save the model, or also the optimizer, scheduler & rng state. Note that when this is true, you won’t be able to resume training from checkpoint. This enables you to save storage by not storing the optimizer, scheduler & rng state. You can only load the model using `from_pretrained` with this option set to `True`.
  * **restore_callback_states_from_checkpoint** (`bool`, _optional_ , defaults to `False`) — Whether to restore the callback states from the checkpoint. If `True`, will override callbacks passed to the `Trainer` if they exist in the checkpoint.”
  * **use_cpu** (`bool`, _optional_ , defaults to `False`) — Whether or not to use cpu. If set to False, we will use cuda or mps device if available.
  * **seed** (`int`, _optional_ , defaults to 42) — Random seed that will be set at the beginning of training. To ensure reproducibility across runs, use the `~Trainer.model_init` function to instantiate the model if it has some randomly initialized parameters.
  * **data_seed** (`int`, _optional_) — Random seed to be used with data samplers. If not set, random generators for data sampling will use the same seed as `seed`. This can be used to ensure reproducibility of data sampling, independent of the model seed.
  * **jit_mode_eval** (`bool`, _optional_ , defaults to `False`) — Whether or not to use PyTorch jit trace for inference.
  * **use_ipex** (`bool`, _optional_ , defaults to `False`) — Use Intel extension for PyTorch when it is available. [IPEX installation](https://github.com/intel/intel-extension-for-pytorch).
  * **bf16** (`bool`, _optional_ , defaults to `False`) — Whether to use bf16 16-bit (mixed) precision training instead of 32-bit training. Requires Ampere or higher NVIDIA architecture or Intel XPU or using CPU (use_cpu) or Ascend NPU. This is an experimental API and it may change.
  * **fp16** (`bool`, _optional_ , defaults to `False`) — Whether to use fp16 16-bit (mixed) precision training instead of 32-bit training.
  * **fp16_opt_level** (`str`, _optional_ , defaults to ‘O1’) — For `fp16` training, Apex AMP optimization level selected in [‘O0’, ‘O1’, ‘O2’, and ‘O3’]. See details on the [Apex documentation](https://nvidia.github.io/apex/amp).
  * **fp16_backend** (`str`, _optional_ , defaults to `"auto"`) — This argument is deprecated. Use `half_precision_backend` instead.
  * **half_precision_backend** (`str`, _optional_ , defaults to `"auto"`) — The backend to use for mixed precision training. Must be one of `"auto", "apex", "cpu_amp"`. `"auto"` will use CPU/CUDA AMP or APEX depending on the PyTorch version detected, while the other choices will force the requested backend.
  * **bf16_full_eval** (`bool`, _optional_ , defaults to `False`) — Whether to use full bfloat16 evaluation instead of 32-bit. This will be faster and save memory but can harm metric values. This is an experimental API and it may change.
  * **fp16_full_eval** (`bool`, _optional_ , defaults to `False`) — Whether to use full float16 evaluation instead of 32-bit. This will be faster and save memory but can harm metric values.
  * **tf32** (`bool`, _optional_) — Whether to enable the TF32 mode, available in Ampere and newer GPU architectures. The default value depends on PyTorch’s version default of `torch.backends.cuda.matmul.allow_tf32`. For more details please refer to the [TF32](https://huggingface.co/docs/transformers/perf_train_gpu_one#tf32) documentation. This is an experimental API and it may change.
  * **local_rank** (`int`, _optional_ , defaults to -1) — Rank of the process during distributed training.
  * **ddp_backend** (`str`, _optional_) — The backend to use for distributed training. Must be one of `"nccl"`, `"mpi"`, `"ccl"`, `"gloo"`, `"hccl"`.
  * **tpu_num_cores** (`int`, _optional_) — When training on TPU, the number of TPU cores (automatically passed by launcher script).
  * **dataloader_drop_last** (`bool`, _optional_ , defaults to `False`) — Whether to drop the last incomplete batch (if the length of the dataset is not divisible by the batch size) or not.
  * **eval_steps** (`int` or `float`, _optional_) — Number of update steps between two evaluations if `eval_strategy="steps"`. Will default to the same value as `logging_steps` if not set. Should be an integer or a float in range `[0,1)`. If smaller than 1, will be interpreted as ratio of total training steps.
  * **dataloader_num_workers** (`int`, _optional_ , defaults to 0) — Number of subprocesses to use for data loading (PyTorch only). 0 means that the data will be loaded in the main process.
  * **past_index** (`int`, _optional_ , defaults to -1) — Some models like [TransformerXL](../model_doc/transformerxl) or [XLNet](../model_doc/xlnet) can make use of the past hidden states for their predictions. If this argument is set to a positive int, the `Trainer` will use the corresponding output (usually index 2) as the past state and feed it to the model at the next training step under the keyword argument `mems`.
  * **run_name** (`str`, _optional_ , defaults to `output_dir`) — A descriptor for the run. Typically used for [wandb](https://www.wandb.com/), [mlflow](https://www.mlflow.org/), [comet](https://www.comet.com/site) and [swanlab](https://swanlab.cn) logging. If not specified, will be the same as `output_dir`.
  * **disable_tqdm** (`bool`, _optional_) — Whether or not to disable the tqdm progress bars and table of metrics produced by `~notebook.NotebookTrainingTracker` in Jupyter Notebooks. Will default to `True` if the logging level is set to warn or lower (default), `False` otherwise.
  * **remove_unused_columns** (`bool`, _optional_ , defaults to `True`) — Whether or not to automatically remove the columns unused by the model forward method.
  * **label_names** (`list[str]`, _optional_) — The list of keys in your dictionary of inputs that correspond to the labels. 

Will eventually default to the list of argument names accepted by the model that contain the word “label”, except if the model used is one of the `XxxForQuestionAnswering` in which case it will also include the `["start_positions", "end_positions"]` keys.

  * **load_best_model_at_end** (`bool`, _optional_ , defaults to `False`) — Whether or not to load the best model found during training at the end of training. When this option is enabled, the best checkpoint will always be saved. See [`save_total_limit`](https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments.save_total_limit) for more. 
  * **metric_for_best_model** (`str`, _optional_) — Use in conjunction with `load_best_model_at_end` to specify the metric to use to compare two different models. Must be the name of a metric returned by the evaluation with or without the prefix `"eval_"`. 

If not specified, this will default to `"loss"` when either `load_best_model_at_end == True` or `lr_scheduler_type == SchedulerType.REDUCE_ON_PLATEAU` (to use the evaluation loss).

If you set this value, `greater_is_better` will default to `True` unless the name ends with “loss”. Don’t forget to set it to `False` if your metric is better when lower.

  * **greater_is_better** (`bool`, _optional_) — Use in conjunction with `load_best_model_at_end` and `metric_for_best_model` to specify if better models should have a greater metric or not. Will default to: 
    * `True` if `metric_for_best_model` is set to a value that doesn’t end in `"loss"`.
    * `False` if `metric_for_best_model` is not set, or set to a value that ends in `"loss"`.
  * **ignore_data_skip** (`bool`, _optional_ , defaults to `False`) — When resuming training, whether or not to skip the epochs and batches to get the data loading at the same stage as in the previous training. If set to `True`, the training will begin faster (as that skipping step can take a long time) but will not yield the same results as the interrupted training would have.
  * **fsdp** (`bool`, `str` or list of `FSDPOption`, _optional_ , defaults to `''`) — Use PyTorch Distributed Parallel Training (in distributed training only). 

A list of options along the following:

    * `"full_shard"`: Shard parameters, gradients and optimizer states.
    * `"shard_grad_op"`: Shard optimizer states and gradients.
    * `"hybrid_shard"`: Apply `FULL_SHARD` within a node, and replicate parameters across nodes.
    * `"hybrid_shard_zero2"`: Apply `SHARD_GRAD_OP` within a node, and replicate parameters across nodes.
    * `"offload"`: Offload parameters and gradients to CPUs (only compatible with `"full_shard"` and `"shard_grad_op"`).
    * `"auto_wrap"`: Automatically recursively wrap layers with FSDP using `default_auto_wrap_policy`.
  * **fsdp_config** (`str` or `dict`, _optional_) — Config to be used with fsdp (Pytorch Distributed Parallel Training). The value is either a location of fsdp json config file (e.g., `fsdp_config.json`) or an already loaded json file as `dict`. 

A List of config and its options:

    * min_num_params (`int`, _optional_ , defaults to `0`): FSDP’s minimum number of parameters for Default Auto Wrapping. (useful only when `fsdp` field is passed).

    * transformer_layer_cls_to_wrap (`list[str]`, _optional_): List of transformer layer class names (case-sensitive) to wrap, e.g, `BertLayer`, `GPTJBlock`, `T5Block` … (useful only when `fsdp` flag is passed).

    * backward_prefetch (`str`, _optional_) FSDP’s backward prefetch mode. Controls when to prefetch next set of parameters (useful only when `fsdp` field is passed).

A list of options along the following:

      * `"backward_pre"` : Prefetches the next set of parameters before the current set of parameter’s gradient computation.
      * `"backward_post"` : This prefetches the next set of parameters after the current set of parameter’s gradient computation.
    * forward_prefetch (`bool`, _optional_ , defaults to `False`) FSDP’s forward prefetch mode (useful only when `fsdp` field is passed). If `"True"`, then FSDP explicitly prefetches the next upcoming all-gather while executing in the forward pass.

    * limit_all_gathers (`bool`, _optional_ , defaults to `False`) FSDP’s limit_all_gathers (useful only when `fsdp` field is passed). If `"True"`, FSDP explicitly synchronizes the CPU thread to prevent too many in-flight all-gathers.

    * use_orig_params (`bool`, _optional_ , defaults to `True`) If `"True"`, allows non-uniform `requires_grad` during init, which means support for interspersed frozen and trainable parameters. Useful in cases such as parameter-efficient fine-tuning. Please refer this [blog](<https://dev-discuss.pytorch.org/t/rethinking-pytorch-fully-sharded-data-parallel-fsdp-from-first-principles/1019>

    * sync_module_states (`bool`, _optional_ , defaults to `True`) If `"True"`, each individually wrapped FSDP unit will broadcast module parameters from rank 0 to ensure they are the same across all ranks after initialization

    * cpu_ram_efficient_loading (`bool`, _optional_ , defaults to `False`) If `"True"`, only the first process loads the pretrained model checkpoint while all other processes have empty weights. When this setting as `"True"`, `sync_module_states` also must to be `"True"`, otherwise all the processes except the main process would have random weights leading to unexpected behaviour during training.

    * activation_checkpointing (`bool`, _optional_ , defaults to `False`): If `"True"`, activation checkpointing is a technique to reduce memory usage by clearing activations of certain layers and recomputing them during a backward pass. Effectively, this trades extra computation time for reduced memory usage.

    * xla (`bool`, _optional_ , defaults to `False`): Whether to use PyTorch/XLA Fully Sharded Data Parallel Training. This is an experimental feature and its API may evolve in the future.

    * xla_fsdp_settings (`dict`, _optional_) The value is a dictionary which stores the XLA FSDP wrapping parameters.

For a complete list of options, please see [here](https://github.com/pytorch/xla/blob/master/torch_xla/distributed/fsdp/xla_fully_sharded_data_parallel.py).

    * xla_fsdp_grad_ckpt (`bool`, _optional_ , defaults to `False`): Will use gradient checkpointing over each nested XLA FSDP wrapped layer. This setting can only be used when the xla flag is set to true, and an auto wrapping policy is specified through fsdp_min_num_params or fsdp_transformer_layer_cls_to_wrap.

  * **deepspeed** (`str` or `dict`, _optional_) — Use [Deepspeed](https://github.com/deepspeedai/DeepSpeed). This is an experimental feature and its API may evolve in the future. The value is either the location of DeepSpeed json config file (e.g., `ds_config.json`) or an already loaded json file as a `dict`” 
  * **accelerator_config** (`str`, `dict`, or `AcceleratorConfig`, _optional_) — Config to be used with the internal `Accelerator` implementation. The value is either a location of accelerator json config file (e.g., `accelerator_config.json`), an already loaded json file as `dict`, or an instance of `AcceleratorConfig`. 

A list of config and its options:

    * split_batches (`bool`, _optional_ , defaults to `False`): Whether or not the accelerator should split the batches yielded by the dataloaders across the devices. If `True` the actual batch size used will be the same on any kind of distributed processes, but it must be a round multiple of the `num_processes` you are using. If `False`, actual batch size used will be the one set in your script multiplied by the number of processes.
    * dispatch_batches (`bool`, _optional_): If set to `True`, the dataloader prepared by the Accelerator is only iterated through on the main process and then the batches are split and broadcast to each process. Will default to `True` for `DataLoader` whose underlying dataset is an `IterableDataset`, `False` otherwise.
    * even_batches (`bool`, _optional_ , defaults to `True`): If set to `True`, in cases where the total batch size across all processes does not exactly divide the dataset, samples at the start of the dataset will be duplicated so the batch can be divided equally among all workers.
    * use_seedable_sampler (`bool`, _optional_ , defaults to `True`): Whether or not use a fully seedable random sampler (`accelerate.data_loader.SeedableRandomSampler`). Ensures training results are fully reproducible using a different sampling technique. While seed-to-seed results may differ, on average the differences are negligible when using multiple different seeds to compare. Should also be ran with `~utils.set_seed` for the best results.
    * use_configured_state (`bool`, _optional_ , defaults to `False`): Whether or not to use a pre-configured `AcceleratorState` or `PartialState` defined before calling `TrainingArguments`. If `True`, an `Accelerator` or `PartialState` must be initialized. Note that by doing so, this could lead to issues with hyperparameter tuning.
  * **label_smoothing_factor** (`float`, _optional_ , defaults to 0.0) — The label smoothing factor to use. Zero means no label smoothing, otherwise the underlying onehot-encoded labels are changed from 0s and 1s to `label_smoothing_factor/num_labels` and `1 - label_smoothing_factor + label_smoothing_factor/num_labels` respectively.
  * **debug** (`str` or list of `DebugOption`, _optional_ , defaults to `""`) — Enable one or more debug features. This is an experimental feature. 

Possible options are:

    * `"underflow_overflow"`: detects overflow in model’s input/outputs and reports the last frames that led to the event
    * `"tpu_metrics_debug"`: print debug metrics on TPU

The options should be separated by whitespaces.

  * **optim** (`str` or `training_args.OptimizerNames`, _optional_ , defaults to `"adamw_torch"`) — The optimizer to use, such as “adamw_torch”, “adamw_torch_fused”, “adamw_apex_fused”, “adamw_anyprecision”, “adafactor”. See `OptimizerNames` in [training_args.py](https://github.com/huggingface/transformers/blob/main/src/transformers/training_args.py) for a full list of optimizers.
  * **optim_args** (`str`, _optional_) — Optional arguments that are supplied to optimizers such as AnyPrecisionAdamW, AdEMAMix, and GaLore.
  * **group_by_length** (`bool`, _optional_ , defaults to `False`) — Whether or not to group together samples of roughly the same length in the training dataset (to minimize padding applied and be more efficient). Only useful if applying dynamic padding.
  * **length_column_name** (`str`, _optional_ , defaults to `"length"`) — Column name for precomputed lengths. If the column exists, grouping by length will use these values rather than computing them on train startup. Ignored unless `group_by_length` is `True` and the dataset is an instance of `Dataset`.
  * **report_to** (`str` or `list[str]`, _optional_ , defaults to `"all"`) — The list of integrations to report the results and logs to. Supported platforms are `"azure_ml"`, `"clearml"`, `"codecarbon"`, `"comet_ml"`, `"dagshub"`, `"dvclive"`, `"flyte"`, `"mlflow"`, `"neptune"`, `"swanlab"`, `"tensorboard"`, and `"wandb"`. Use `"all"` to report to all integrations installed, `"none"` for no integrations.
  * **ddp_find_unused_parameters** (`bool`, _optional_) — When using distributed training, the value of the flag `find_unused_parameters` passed to `DistributedDataParallel`. Will default to `False` if gradient checkpointing is used, `True` otherwise.
  * **ddp_bucket_cap_mb** (`int`, _optional_) — When using distributed training, the value of the flag `bucket_cap_mb` passed to `DistributedDataParallel`.
  * **ddp_broadcast_buffers** (`bool`, _optional_) — When using distributed training, the value of the flag `broadcast_buffers` passed to `DistributedDataParallel`. Will default to `False` if gradient checkpointing is used, `True` otherwise.
  * **dataloader_pin_memory** (`bool`, _optional_ , defaults to `True`) — Whether you want to pin memory in data loaders or not. Will default to `True`.
  * **dataloader_persistent_workers** (`bool`, _optional_ , defaults to `False`) — If True, the data loader will not shut down the worker processes after a dataset has been consumed once. This allows to maintain the workers Dataset instances alive. Can potentially speed up training, but will increase RAM usage. Will default to `False`.
  * **dataloader_prefetch_factor** (`int`, _optional_) — Number of batches loaded in advance by each worker. 2 means there will be a total of 2 * num_workers batches prefetched across all workers.
  * **skip_memory_metrics** (`bool`, _optional_ , defaults to `True`) — Whether to skip adding of memory profiler reports to metrics. This is skipped by default because it slows down the training and evaluation speed.
  * **push_to_hub** (`bool`, _optional_ , defaults to `False`) — Whether or not to push the model to the Hub every time the model is saved. If this is activated, `output_dir` will begin a git directory synced with the repo (determined by `hub_model_id`) and the content will be pushed each time a save is triggered (depending on your `save_strategy`). Calling [save_model()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.save_model) will also trigger a push. 
  * **resume_from_checkpoint** (`str`, _optional_) — The path to a folder with a valid checkpoint for your model. This argument is not directly used by [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer), it’s intended to be used by your training/evaluation scripts instead. See the [example scripts](https://github.com/huggingface/transformers/tree/main/examples) for more details.
  * **hub_model_id** (`str`, _optional_) — The name of the repository to keep in sync with the local _output_dir_. It can be a simple model ID in which case the model will be pushed in your namespace. Otherwise it should be the whole repository name, for instance `"user_name/model"`, which allows you to push to an organization you are a member of with `"organization_name/model"`. Will default to `user_name/output_dir_name` with _output_dir_name_ being the name of `output_dir`. 

Will default to the name of `output_dir`.

  * **hub_strategy** (`str` or `HubStrategy`, _optional_ , defaults to `"every_save"`) — Defines the scope of what is pushed to the Hub and when. Possible values are: 
    * `"end"`: push the model, its configuration, the processing class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card when the [save_model()](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer.save_model) method is called.
    * `"every_save"`: push the model, its configuration, the processing class e.g. tokenizer (if passed along to the [Trainer](/docs/transformers/v4.53.1/en/main_classes/trainer#transformers.Trainer)) and a draft of a model card each time there is a model save. The pushes are asynchronous to not block training, and in case the save are very frequent, a new push is only attempted if the previous one is finished. A last push is made with the final model at the end of training.
    * `"checkpoint"`: like `"every_save"` but the latest checkpoint is also pushed in a subfolder named last-checkpoint, allowing you to resume training easily with `trainer.train(resume_from_checkpoint="last-checkpoint")`.
    * `"all_checkpoints"`: like `"checkpoint"` but all checkpoints are pushed like they appear in the output folder (so you will get one checkpoint folder per folder in your final repository)
  * **hub_token** (`str`, _optional_) — The token to use to push the model to the Hub. Will default to the token in the cache folder obtained with `huggingface-cli login`.
  * **hub_private_repo** (`bool`, _optional_) — Whether to make the repo private. If `None` (default), the repo will be public unless the organization’s default is private. This value is ignored if the repo already exists.
  * **hub_always_push** (`bool`, _optional_ , defaults to `False`) — Unless this is `True`, the `Trainer` will skip pushing a checkpoint when the previous push is not finished.
  * **hub_revision** (`str`, _optional_) — The revision to use when pushing to the Hub. Can be a branch name, a tag, or a commit hash.
  * **gradient_checkpointing** (`bool`, _optional_ , defaults to `False`) — If True, use gradient checkpointing to save memory at the expense of slower backward pass.
  * **gradient_checkpointing_kwargs** (`dict`, _optional_ , defaults to `None`) — Key word arguments to be passed to the `gradient_checkpointing_enable` method.
  * **include_inputs_for_metrics** (`bool`, _optional_ , defaults to `False`) — This argument is deprecated. Use `include_for_metrics` instead, e.g, `include_for_metrics = ["inputs"]`.
  * **include_for_metrics** (`list[str]`, _optional_ , defaults to `[]`) — Include additional data in the `compute_metrics` function if needed for metrics computation. Possible options to add to `include_for_metrics` list: 
    * `"inputs"`: Input data passed to the model, intended for calculating input dependent metrics.
    * `"loss"`: Loss values computed during evaluation, intended for calculating loss dependent metrics.
  * **eval_do_concat_batches** (`bool`, _optional_ , defaults to `True`) — Whether to recursively concat inputs/losses/labels/predictions across batches. If `False`, will instead store them as lists, with each batch kept separate.
  * **auto_find_batch_size** (`bool`, _optional_ , defaults to `False`) — Whether to find a batch size that will fit into memory automatically through exponential decay, avoiding CUDA Out-of-Memory errors. Requires accelerate to be installed (`pip install accelerate`)
  * **full_determinism** (`bool`, _optional_ , defaults to `False`) — If `True`, [enable_full_determinism()](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.enable_full_determinism) is called instead of [set_seed()](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.set_seed) to ensure reproducible results in distributed training. Important: this will negatively impact the performance, so only use it for debugging.
  * **torchdynamo** (`str`, _optional_) — If set, the backend compiler for TorchDynamo. Possible choices are `"eager"`, `"aot_eager"`, `"inductor"`, `"nvfuser"`, `"aot_nvfuser"`, `"aot_cudagraphs"`, `"ofi"`, `"fx2trt"`, `"onnxrt"` and `"ipex"`.
  * **ray_scope** (`str`, _optional_ , defaults to `"last"`) — The scope to use when doing hyperparameter search with Ray. By default, `"last"` will be used. Ray will then use the last checkpoint of all trials, compare those, and select the best one. However, other options are also available. See the [Ray documentation](https://docs.ray.io/en/latest/tune/api_docs/analysis.html#ray.tune.ExperimentAnalysis.get_best_trial) for more options.
  * **ddp_timeout** (`int`, _optional_ , defaults to 1800) — The timeout for `torch.distributed.init_process_group` calls, used to avoid GPU socket timeouts when performing slow operations in distributed runnings. Please refer the [PyTorch documentation] (<https://pytorch.org/docs/stable/distributed.html#torch.distributed.init_process_group>) for more information.
  * **use_mps_device** (`bool`, _optional_ , defaults to `False`) — This argument is deprecated.`mps` device will be used if it is available similar to `cuda` device.
  * **torch_compile** (`bool`, _optional_ , defaults to `False`) — Whether or not to compile the model using PyTorch 2.0 [`torch.compile`](https://pytorch.org/get-started/pytorch-2.0/). 

This will use the best defaults for the [`torch.compile` API](https://pytorch.org/docs/stable/generated/torch.compile.html?highlight=torch+compile#torch.compile). You can customize the defaults with the argument `torch_compile_backend` and `torch_compile_mode` but we don’t guarantee any of them will work as the support is progressively rolled in in PyTorch.

This flag and the whole compile API is experimental and subject to change in future releases.

  * **torch_compile_backend** (`str`, _optional_) — The backend to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`. 

Refer to the PyTorch doc for possible values and note that they may change across PyTorch versions.

This flag is experimental and subject to change in future releases.

  * **torch_compile_mode** (`str`, _optional_) — The mode to use in `torch.compile`. If set to any value, `torch_compile` will be set to `True`. 

Refer to the PyTorch doc for possible values and note that they may change across PyTorch versions.

This flag is experimental and subject to change in future releases.

  * **include_tokens_per_second** (`bool`, _optional_) — Whether or not to compute the number of tokens per second per device for training speed metrics. 

This will iterate over the entire training dataloader once beforehand,

and will slow down the entire process.

  * **include_num_input_tokens_seen** (`bool`, _optional_) — Whether or not to track the number of input tokens seen throughout training. 

May be slower in distributed training as gather operations must be called.

  * **neftune_noise_alpha** (`Optional[float]`) — If not `None`, this will activate NEFTune noise embeddings. This can drastically improve model performance for instruction fine-tuning. Check out the [original paper](https://huggingface.co/papers/2310.05914) and the [original code](https://github.com/neelsjain/NEFTune). Support transformers `PreTrainedModel` and also `PeftModel` from peft. The original paper used values in the range [5.0, 15.0].
  * **optim_target_modules** (`Union[str, list[str]]`, _optional_) — The target modules to optimize, i.e. the module names that you would like to train. Currently used for the GaLore algorithm (<https://huggingface.co/papers/2403.03507>) and APOLLO algorithm (<https://huggingface.co/papers/2412.05270>). See GaLore implementation (<https://github.com/jiaweizzhao/GaLore>) and APOLLO implementation (<https://github.com/zhuhanqing/APOLLO>) for more details. You need to make sure to pass a valid GaLore or APOLLO optimizer, e.g., one of: “apollo_adamw”, “galore_adamw”, “galore_adamw_8bit”, “galore_adafactor” and make sure that the target modules are `nn.Linear` modules only.
  * **batch_eval_metrics** (`Optional[bool]`, defaults to `False`) — If set to `True`, evaluation will call compute_metrics at the end of each batch to accumulate statistics rather than saving all eval logits in memory. When set to `True`, you must pass a compute_metrics function that takes a boolean argument `compute_result`, which when passed `True`, will trigger the final global summary statistics from the batch-level summary statistics you’ve accumulated over the evaluation set.
  * **eval_on_start** (`bool`, _optional_ , defaults to `False`) — Whether to perform a evaluation step (sanity check) before the training to ensure the validation steps works correctly.
  * **eval_use_gather_object** (`bool`, _optional_ , defaults to `False`) — Whether to run recursively gather object in a nested list/tuple/dictionary of objects from all devices. This should only be enabled if users are not just returning tensors, and this is actively discouraged by PyTorch.
  * **use_liger_kernel** (`bool`, _optional_ , defaults to `False`) — Whether enable [Liger](https://github.com/linkedin/Liger-Kernel) Kernel for LLM model training. It can effectively increase multi-GPU training throughput by ~20% and reduces memory usage by ~60%, works out of the box with flash attention, PyTorch FSDP, and Microsoft DeepSpeed. Currently, it supports llama, mistral, mixtral and gemma models.
  * **liger_kernel_config** (`Optional[dict]`, _optional_) — Configuration to be used for Liger Kernel. When use_liger_kernel=True, this dict is passed as keyword arguments to the `_apply_liger_kernel_to_instance` function, which specifies which kernels to apply. Available options vary by model but typically include: ‘rope’, ‘swiglu’, ‘cross_entropy’, ‘fused_linear_cross_entropy’, ‘rms_norm’, etc. If `None`, use the default kernel configurations.
  * **average_tokens_across_devices** (`bool`, _optional_ , defaults to `False`) — Whether or not to average tokens across devices. If enabled, will use all_reduce to synchronize num_tokens_in_batch for precise loss calculation. Reference: <https://github.com/huggingface/transformers/issues/34242>
  * **predict_with_generate** (`bool`, _optional_ , defaults to `False`) — Whether to use generate to calculate generative metrics (ROUGE, BLEU).
  * **generation_max_length** (`int`, _optional_) — The `max_length` to use on each evaluation loop when `predict_with_generate=True`. Will default to the `max_length` value of the model configuration.
  * **generation_num_beams** (`int`, _optional_) — The `num_beams` to use on each evaluation loop when `predict_with_generate=True`. Will default to the `num_beams` value of the model configuration.
  * **generation_config** (`str` or `Path` or [GenerationConfig](/docs/transformers/v4.53.1/en/main_classes/text_generation#transformers.GenerationConfig), _optional_) — Allows to load a [GenerationConfig](/docs/transformers/v4.53.1/en/main_classes/text_generation#transformers.GenerationConfig) from the `from_pretrained` method. This can be either: 
    * a string, the _model id_ of a pretrained model configuration hosted inside a model repo on huggingface.co.
    * a path to a _directory_ containing a configuration file saved using the [save_pretrained()](/docs/transformers/v4.53.1/en/main_classes/text_generation#transformers.GenerationConfig.save_pretrained) method, e.g., `./my_model_directory/`.
    * a [GenerationConfig](/docs/transformers/v4.53.1/en/main_classes/text_generation#transformers.GenerationConfig) object.

TrainingArguments is the subset of the arguments we use in our example scripts **which relate to the training loop itself**.

Using [HfArgumentParser](/docs/transformers/v4.53.1/en/internal/trainer_utils#transformers.HfArgumentParser) we can turn this class into [argparse](https://docs.python.org/3/library/argparse#module-argparse) arguments that can be specified on the command line.

Serializes this instance while replace `Enum` by their values and `GenerationConfig` by dictionaries (for JSON serialization support). It obfuscates the token values by removing their value.

[< > Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/main_classes/trainer.md)