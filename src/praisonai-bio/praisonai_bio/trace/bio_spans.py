"""Trace span attributes for BioModels workflows."""

BIO_SPAN_ATTRS = {
    "BIOMODELS_SEARCH": ["query", "num_results"],
    "SIMULATION_RUN": ["model_id", "duration"],
    "PERTURBATION_COMPLETE": ["parameter", "value"],
    "REPRO_EXPORT": ["model_id", "bundle_dir"],
}
