"""

"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: BSD-3-Clause

Pedestrian = {
    "Autoformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 64,
        "d_ffn": 512,
        "n_heads": 4,
        "factor": 3,
        "moving_avg_window_size": 13,
        "dropout": 0,
        "lr": 0.0007192898298984755,
    },
    "BRITS": {
        "n_steps": 24,
        "n_features": 1,
        "patience": 10,
        "epochs": 100,
        "rnn_hidden_size": 1024,
        "lr": 0.0021412312914315347,
    },
    "Crossformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 2,
        "d_model": 64,
        "d_ffn": 128,
        "n_heads": 2,
        "factor": 5,
        "seg_len": 6,
        "win_size": 4,
        "dropout": 0.2,
        "lr": 0.000931609728448281,
    },
    "CSDI": {
        "n_steps": 24,
        "n_features": 1,
        "patience": 10,
        "epochs": 100,
        "n_layers": 3,
        "n_heads": 2,
        "n_channels": 64,
        "d_time_embedding": 256,
        "d_feature_embedding": 32,
        "d_diffusion_embedding": 32,
        "lr": 0.0009538000135184797,
    },
    "DLinear": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "moving_avg_window_size": 25,
        "d_model": 256,
        "lr": 0.0011808310946287465,
    },
    "ETSformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_e_layers": 2,
        "n_d_layers": 2,
        "d_model": 256,
        "d_ffn": 256,
        "n_heads": 4,
        "top_k": 3,
        "dropout": 0,
        "lr": 0.0034456093299020424,
    },
    "FiLM": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "window_size": [2],
        "multiscale": [1, 2],
        "modes1": 64,
        "dropout": 0.1,
        "mode_type": 1,
        "d_model": 1024,
        "lr": 0.008783320870673158,
    },
    "FreTS": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "embed_size": 64,
        "hidden_size": 64,
        "channel_independence": True,
        "lr": 0.001899974579055577,
    },
    "GPVAE": {
        "n_steps": 24,
        "n_features": 1,
        "latent_size": 1,
        "patience": 10,
        "epochs": 100,
        "lr": 0.004720864493340685,
        "beta": 0.2,
        "sigma": 1.005,
        "length_scale": 7,
        "encoder_sizes": [512, 512],
        "decoder_sizes": [128, 128],
        "window_size": 6,
    },
    "GRUD": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "rnn_hidden_size": 128,
        "lr": 0.009156381444194367,
    },
    "Informer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 64,
        "d_ffn": 1024,
        "n_heads": 1,
        "factor": 5,
        "dropout": 0.1,
        "lr": 0.00031522812820120077,
    },
    "iTransformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 1,
        "d_model": 256,
        "d_ffn": 2048,
        "n_heads": 8,
        "d_k": 64,
        "d_v": 32,
        "dropout": 0.1,
        "attn_dropout": 0.1,
        "lr": 0.00015714210596319564,
    },
    "Koopa": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_seg_steps": 12,
        "d_dynamic": 128,
        "d_hidden": 128,
        "n_hidden_layers": 1,
        "n_blocks": 3,
        "lr": 0.003749596878156908,
    },
    "MICN": None,
    "MRNN": {
        "n_steps": 24,
        "n_features": 1,
        "patience": 10,
        "epochs": 100,
        "rnn_hidden_size": 256,
        "lr": 0.00988986364396156,
    },
    "NonstationaryTransformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 1,
        "d_model": 1024,
        "n_heads": 8,
        "d_ffn": 1024,
        "n_projector_hidden_layers": 2,
        "d_projector_hidden": [128, 128],
        "dropout": 0.5,
        "lr": 0.0020427141117888192,
    },
    "PatchTST": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "patch_len": 16,
        "stride": 4,
        "n_layers": 2,
        "d_model": 64,
        "d_ffn": 256,
        "n_heads": 2,
        "d_k": 32,
        "d_v": 32,
        "dropout": 0.1,
        "attn_dropout": 0.1,
        "lr": 0.00039859557106126415,
    },
    "Pyraformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 256,
        "d_ffn": 64,
        "n_heads": 4,
        "window_size": [4, 4],
        "inner_size": 5,
        "dropout": 0,
        "attn_dropout": 0.1,
        "lr": 0.00011756849789619954,
    },
    "SAITS": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 2,
        "d_model": 64,
        "d_ffn": 128,
        "n_heads": 2,
        "d_k": 32,
        "d_v": 32,
        "dropout": 0,
        "attn_dropout": 0.4,
        "lr": 0.0008997246974123553,
    },
    "SCINet": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_stacks": 1,
        "n_levels": 2,
        "n_groups": 1,
        "n_decoder_layers": 2,
        "d_hidden": 512,
        "dropout": 0,
        "lr": 0.0005451559336372225,
    },
    "StemGNN": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "n_stacks": 1,
        "d_model": 512,
        "dropout": 0.1,
        "lr": 0.000934754276624635,
    },
    "TimesNet": {
        "n_steps": 24,
        "n_features": 1,
        "patience": 10,
        "epochs": 100,
        "n_layers": 1,
        "top_k": 5,
        "d_model": 128,
        "d_ffn": 256,
        "n_kernels": 5,
        "dropout": 0,
        "lr": 0.00012645341855846453,
    },
    "Transformer": {
        "n_steps": 24,
        "n_features": 1,
        "epochs": 100,
        "patience": 10,
        "n_layers": 5,
        "d_model": 1024,
        "d_ffn": 2048,
        "n_heads": 4,
        "d_k": 128,
        "d_v": 32,
        "dropout": 0.1,
        "attn_dropout": 0.2,
        "lr": 0.00013157218692030537,
    },
    "USGAN": {
        "n_steps": 24,
        "n_features": 1,
        "patience": 10,
        "epochs": 100,
        "lr": 0.003419261881553021,
        "rnn_hidden_size": 1024,
        "dropout": 0.2,
    },
}
