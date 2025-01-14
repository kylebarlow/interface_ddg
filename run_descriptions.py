class ddg_benchmark_run:
    def __init__(self, prediction_set_name, step_multiplication_factor):
        self.prediction_set_name = prediction_set_name
        self.step_multiplication_factor = step_multiplication_factor

talaris_60k_run = ddg_benchmark_run(
    'zemu_1.2-60000_rscript_validated-t14', # Predicton run name
    5 # Step multiplication factor
)

talaris_60k_simplified = ddg_benchmark_run(
    'zemu_1.2-60000_rscript_simplified-t14', # Predicton run name
    5 # Step multiplication factor
)

talaris_60k_16_simplified = ddg_benchmark_run(
    'zemu_1.6-60000_rscript_simplified-t14', # Predicton run name
    5 # Step multiplication factor
)

talaris_control_run = ddg_benchmark_run(
    'zemu_control', # Predicton run name
    1 # Step multiplication factor
)

control_run_69aa526_noglypivot = ddg_benchmark_run(
    'zemu_control-69aa526-noglypivot', # Predicton run name
    1 # Step multiplication factor
)

control_run_69aa526 = ddg_benchmark_run(
    'zemu_control-69aa526', # Predicton run name
    1 # Step multiplication factor
)

ref_run = ddg_benchmark_run(
    'zemu_1.2-60000_rscript_validated-ref', # Predicton run name
    5 # Step multiplication factor
)

ref_run_cart = ddg_benchmark_run(
    'zemu_1.2-60000_rscript_validated-ref-cart', # Predicton run name
    5 # Step multiplication factor
)

ddg_monomer_run = ddg_benchmark_run(
    'ddg_monomer_16_003-zemu-2',
    1
)

zemu_values = ddg_benchmark_run(
    'zemu-values',
    1
)

temp_16 = ddg_benchmark_run(
    'zemu-brub_1.6-nt10000',
    1250
)

all_runs = [
    talaris_60k_16_simplified,
    ref_run_cart,
    ref_run,
    zemu_values,
    ddg_monomer_run,
    talaris_control_run,
    talaris_60k_run,
    talaris_60k_simplified,
    temp_16,
    control_run_69aa526_noglypivot,
    control_run_69aa526,
]
