# Contributing

Thank you for improving the Airflow Cookbook. Keep examples small, reproducible, and honest about what has actually been tested.

## Scope

- Prefer synthetic or public data and examples that can be run without private services.
- Do not include credentials, private endpoints, participant data, or production dataset extracts.
- Keep external writes disabled by default. Clearly label placeholders and any step that could mutate a real system.
- Document supported Airflow/Python versions and environment assumptions.
- Do not describe an example as runtime-validated or production-ready without recorded evidence.

## Before opening a pull request

1. Read the relevant example and preserve its stated safety boundaries.
2. Run Python syntax checks with the target Python interpreter where available.
3. In a disposable Airflow environment, run DAG import checks and the example's documented commands when feasible.
4. Record exactly which checks ran, their environment/version, and any checks that could not be run.
5. Check Markdown links and ensure new documentation links to relevant related patterns.

A static syntax check is not a substitute for Airflow import, task execution, or integration testing. If the required environment is unavailable, state that limitation rather than implying the example passed.

## Security issues

Do not report exploitable vulnerabilities in a public issue. Contact zqmcomputing@gmail.com privately with a concise description and reproduction details that do not expose secrets or private data.

## License

By contributing, you agree that your contribution is distributed under the repository's MIT license.
