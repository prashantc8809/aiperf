# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Constants specific to GPU telemetry collection."""

from aiperf.common.enums.metric_enums import (
    EnergyMetricUnit,
    GenericMetricUnit,
    MetricSizeUnit,
    MetricTimeUnit,
    MetricUnitT,
    PowerMetricUnit,
    TemperatureMetricUnit,
)

# Unit conversion scaling factors
SCALING_FACTORS = {
    "energy_consumption": 1e-9,  # mJ to MJ
    "gpu_memory_used": 1.048576 * 1e-3,  # MiB to GB
}

# DCGM field mapping to telemetry record fields
DCGM_TO_FIELD_MAPPING = {
    "DCGM_FI_DEV_POWER_USAGE": "gpu_power_usage",
    "DCGM_FI_DEV_TOTAL_ENERGY_CONSUMPTION": "energy_consumption",
    "DCGM_FI_DEV_GPU_UTIL": "gpu_utilization",
    "DCGM_FI_DEV_FB_USED": "gpu_memory_used",
    "DCGM_FI_DEV_GPU_TEMP": "gpu_temperature",
    "DCGM_FI_DEV_XID_ERRORS": "xid_errors",
    "DCGM_FI_DEV_POWER_VIOLATION": "power_violation",
    "DCGM_FI_DEV_MEM_COPY_UTIL": "mem_copy_util",
    "DCGM_FI_PROF_DRAM_ACTIVE": "dram_active",
    "DCGM_FI_PROF_SM_ACTIVE": "sm_active",
    "DCGM_FI_PROF_SM_OCCUPANCY": "sm_occupancy",
    "DCGM_FI_PROF_PIPE_TENSOR_ACTIVE": "tensor_active",
    "DCGM_FI_PROF_PIPE_FP16_ACTIVE": "fp16_active",
    "DCGM_FI_PROF_GR_ENGINE_ACTIVE": "gr_engine_active",
    "DCGM_FI_PROF_PCIE_TX_BYTES": "pcie_tx_bytes",
    "DCGM_FI_PROF_PCIE_RX_BYTES": "pcie_rx_bytes",
    "DCGM_FI_DEV_CLOCK_THROTTLE_REASONS": "clock_throttle_reasons",
}

# GPU Telemetry Metrics Configuration
# Format: (display_name, field_name, unit_enum)
# - display_name: Human-readable metric name shown in outputs
# - field_name: Corresponds to TelemetryMetrics model field name
# - unit_enum: MetricUnitT enum (use .value in exporters to get string)
GPU_TELEMETRY_METRICS_CONFIG: list[tuple[str, str, MetricUnitT]] = [
    ("GPU Power Usage", "gpu_power_usage", PowerMetricUnit.WATT),
    ("Energy Consumption", "energy_consumption", EnergyMetricUnit.MEGAJOULE),
    ("GPU Utilization", "gpu_utilization", GenericMetricUnit.PERCENT),
    ("GPU Memory Used", "gpu_memory_used", MetricSizeUnit.GIGABYTES),
    ("GPU Temperature", "gpu_temperature", TemperatureMetricUnit.CELSIUS),
    ("XID Errors", "xid_errors", GenericMetricUnit.COUNT),
    ("Power Violation", "power_violation", MetricTimeUnit.MICROSECONDS),
    ("Memory Copy Util", "mem_copy_util", GenericMetricUnit.PERCENT),
    ("DRAM Active", "dram_active", GenericMetricUnit.PERCENT),
    ("SM Active", "sm_active", GenericMetricUnit.PERCENT),
    ("SM Occupancy", "sm_occupancy", GenericMetricUnit.PERCENT),
    ("Tensor Active", "tensor_active", GenericMetricUnit.PERCENT),
    ("FP16 Active", "fp16_active", GenericMetricUnit.PERCENT),
    ("GR Engine Active", "gr_engine_active", GenericMetricUnit.PERCENT),
    ("PCIe TX Bytes", "pcie_tx_bytes", MetricSizeUnit.BYTES),
    ("PCIe RX Bytes", "pcie_rx_bytes", MetricSizeUnit.BYTES),
    ("Clock Throttle Reasons", "clock_throttle_reasons", GenericMetricUnit.COUNT),
]


def get_gpu_telemetry_metrics_config() -> list[tuple[str, str, MetricUnitT]]:
    """Get the current GPU telemetry metrics configuration."""
    return GPU_TELEMETRY_METRICS_CONFIG
