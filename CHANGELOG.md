# Changelog


## [1.4.0] - 2026-07-20

- Remove support for `solcast[all]` for Python 3.8 on Windows due to https://github.com/andfoy/pywinpty/issues/486. 
Note: Plain `solcast` works as it has only uses python built-in packages.
- Update 3.4 Rooftop PV Tuning notebook with more robust handling of azimuth and tilt values.
- Update `test_list_pv_power_sites` to match change in API response format.

## [1.3.1] - 2025-11-19

- Add the `Kimber` and `HSU` to live, forecast, and historic module

## [1.3.0] - 2024-07-10

- Add the `aggregations` module. No tests as we are yet to expose unmetered aggregations.

## [1.2.5] - 2024-07-05

- Add advanced_pv_power to the historic module

## [1.2.4] - 2024-04-19

- Add pv_power_sites to package \_\_init\_\_

## [1.2.2] - 2024-02-28

- Add example notebook showing use of `pv_power_sites` module
- Bug fix for handling Response Code 204 (valid no content)

## [1.2.1] - 2024-02-12

- Remove `to_pandas` method from `pv_power_sites` responses
- Add documentation for `pv_power_sites` module

## [1.2.0] - 2024-01-15

- Add `pv_power_sites` module to enable advanced PV power site configuration
