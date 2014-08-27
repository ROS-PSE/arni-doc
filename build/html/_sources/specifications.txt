Specifications
**************

Specifications are saved to the parameterserver into the namespace ``/arni/specifications``. They are expected in the following format::

    - n!example_node: # a seuid
        measurement1: [minvalue, maxvalue]
        # or
        measurement2: [value, deviation, "relative"]

Available measurement keys are listed below:

Nodes
=====
* node_cpu_usage_mean (float32)
* node_cpu_usage_stddev (float32)
* node_cpu_usage_max (float32)

* node_cpu_usage_core_mean  (float32[])
* node_cpu_usage_core_stddev  (float32[])
* node_cpu_usage_core_max  (float32[])

* node_gpu_usage_mean  (float32[])
* node_gpu_usage_stddev  (float32[])
* node_gpu_usage_max  (float32[])

* node_ramusage_mean  (float32)
* node_ramusage_stddev  (float32)
* node_ramusage_max  (float32)

* node_message_frequency_mean (float32)
* node_message_frequency_stddev (float32)
* node_message_frequency_max (float32)
* node_bandwidth_mean (float32)
* node_bandwidth_stddev (float32)
* node_bandwidth_max (float32)

* node_write_mean (float32)
* node_write_stddev (float32)
* node_write_max (float32)
* node_read_mean (float32)
* node_read_stddev (float32)
* node_read_max (float32)

Hosts
=====
* cpu_temp_mean (float32)
* cpu_temp_stddev (float32)
* cpu_temp_max (float32)
* cpu_usage_mean (float32)
* cpu_usage_stddev (float32)
* cpu_usage_max (float32)
* cpu_usage_core_mean (float32[])
* cpu_usage_core_stddev (float32[])
* cpu_usage_core_max (float32[])
* cpu_temp_core (float32[])
* cpu_temp_core_mean (float32[])
* cpu_temp_core_stddev (float32[])
* cpu_temp_core_max (float32[])

* gpu_temp_mean (float32[])
* gpu_temp_stddev (float32[])
* gpu_temp_max (float32[])
* gpu_usage_mean (float32[])
* gpu_usage_stddev (float32[])
* gpu_usage_max (float32[])

* ram_usage_mean (float32)
* ram_usage_stddev (float32)
* ram_usage_max (float32)

* interface_name (string[])
* message_frequency_mean (float32[])
* message_frequency_stddev (float32[])
* message_frequency_max (float32[])

* bandwidth_mean (float32[])
* bandwidth_stddev (float32[])
* bandwidth_max (float32[])

* drive_name (string[])
* drive_free_space (float32[])

* drive_read (float32[])
* drive_write  (float32[])

Connections
===========
* dropped_msgs (int32)
* traffic (int32)
* period_mean (duration)
* period_stddev (duration)
* period_max (duration)
* stamp_age_mean (duration)
* stamp_age_stddev (duration)
* stamp_age_max (duration)

Topics
======
* dropped_msgs (int)
* traffic (float)
* bandwidth (float)
* stamp_age_max (time)
* stamp_age_mean (time)
* packages (int)
* packages_per_second (float)
