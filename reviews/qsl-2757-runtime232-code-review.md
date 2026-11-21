---
id: "SR-202611210022442313144108518"
title: "Runtime PR232 code-review"
type: SpecReview
analysis: code-review
scope: "agent-ix/filament-contract-runtime; Cargo.toml, Cargo.lock, measurement/exact-panic/Cargo.toml, tools/kernel-api-check/Cargo.toml, tests/exact_outcome_consumer.rs; QSL-2757"
review_set: subset
relationships:
  - target: ix://agent-ix/filament-contract-runtime
    type: references
---

## Summary

Ticket QSL-2757; PR filament-contract-runtime#232; frozen head 7418b09f62196f43f5691aa87b6cec9b8e4b87c7 against 284cb6df9e2c917deba987d952e47e5ffc384ca1. Independent static review; exact model id unavailable. No builds, Cargo tests, runtime reruns, source edits or commits performed.

## Verdict

**PASS** — No new source defect identified in the authorized qualification and cohort prerequisite.

## Findings

| ID | Severity | Summary | Refs |
| --- | --- | --- | --- |
| FND-001 | low | No findings (placeholder) | - |

## Coverage

All root production/dev/allocator, measurement/exact-panic and tools/kernel-api-check direct edges use the requested exact a58474cc105a86f3307a11def3fc001e2459679f / SV 31d807ccb8ffd5a88beb0b1a570b80acb099f5e9 cohort. The SV dependency itself pins the same exact revision. Direct lock inspection finds one entry each for exact, semantic-value, canonical, canonical-derive and qualification. Qualification changes from v0.1.0 to public authoritative ac130b973b1815221cc01a86723f79f0007fd11d, version 0.1.1, without local copies. Read-only git-show comparison confirms 65 old charge points preserved as the prefix of 66, model.candidate last, and all 11 undeclared controls unchanged; the consumed limit-kind vector is byte-identical. The test still imports VALUE_ACCOUNTING_CHARGE_POINT_VECTORS from its published library, requires exact full set equality and uniqueness, checks each code round trip and negative spelling, and retains the exhaustive match with explicit ModelCandidate. There is no wildcard, filtered oracle, private fixture or local replacement vocabulary. The match enumerates owner variants as a compile-time consumer check rather than defining a second owner type or constant. Existing trace binders and assertions are unchanged.

No source, spec, trace tag, gate or fixture body was removed. The bare-metal fixture genuinely has zero tests/benches; its existing test=false and bench=false are unchanged. No new public API, wire format, unsafe code, panic path, resource behavior or engine implementation is introduced. Dependency identity and unchanged consumer assertions are the relevant Rust concerns. FR-275-AC-4 still says branch=main: ARCH's explicit exact/SV revision instruction supersedes that spelling for this wave, not a claim of literal AC-4 compliance or approval of inherited trace counts. QSL-2757 remains open until the four fresh CLI cases pass through matched codegen and the same driver225; this prerequisite alone cannot close it.

## Verification Evidence

ROOT supplied Titan service evidence, not independently rerun: source a0df4061 host exact all-targets check exit 0; runtime lib 8, five integrations 41, kernel API lib 2/doc 5 = 56 passed, 0 failed/ignored. Installed +1.98.1 thumbv7em-none-eabi exact-panic all-target check and documented deployment build exit 0. Qualification-only follow-up 7418b09 exact_outcome_consumer executed both tests, 2 passed/0 failed/ignored/filtered, including authoritative 66-point equality; total 58. Final current-main all-target compiler checks, isolated fixed b68 FSL analyze/root checks and match-head merge freshness belong to ROOT after custody. Full gates, feature sweep, proofs/Kani, benchmarks and installs excluded by dispatch.

Static git diff --check and rustfmt --check --edition 2021 tests/exact_outcome_consumer.rs both exit 0. No applicable AssuranceProfile was found. Spec/plan review methods do not apply because no spec/plan file changed. Optional semantic gap pass skipped.

Tool provenance on terra: /home/peter/.npm-global/bin/quire 0.52.0 (engine 0.62.2); /home/peter/.npm-global/bin/quoin 0.36.8; spec-artifacts-process@v0.36.0. These differ from the supplied release notice; reported to ROOT. No fallback binaries used.

## Examined Scope

```json
[
  {
    "id": "FR-006-AC-1",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "The four outcome dispositions are distinct; completed `false` is a value. `Refusal` and `Undefined` are closed enums; `Incomplete` is a typed record whose reason uses the closed `LimitKind` and `ChargePoint` enums. The runtime consumes these kernel types directly under FR-275."
  },
  {
    "id": "FR-006-AC-3",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Every charge point and limit kind round-trips its QSpec spelling; charges precede work; size counters are high-water, work/result cumulative; the first short counter in field order is reported with the exact denied amount."
  },
  {
    "id": "FR-275-AC-3",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`filament-exact` is an optional dependency of the runtime, enabled only by the `exact` feature."
  },
  {
    "id": "FR-275-AC-4",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The optional `filament-exact` and `filament-semantic-value` dependencies use their own `agent-ix` Git repositories with `branch = \"main\"` and no `rev`, `tag`, `path` or committed `[patch]`."
  },
  {
    "id": "FR-275-AC-5",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`Cargo.lock` holds exactly one entry each for `filament-exact`, `filament-semantic-value`, `quire-canonical` and `quire-canonical-derive`, and, after AD-004 step 5, the FSL-owned evaluation leaf."
  },
  {
    "id": "FR-275-AC-9",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "With `exact` enabled and `std` disabled, the runtime builds for `thumbv7em-none-eabi`. The row `build-exact-no-std-msrv` builds it on the root `Cargo.toml` `rust-version` floor."
  },
  {
    "id": "FR-275-AC-14",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The kernel move deletes no requirement, acceptance criterion or test case."
  },
  {
    "id": "Cargo.toml",
    "path": "Cargo.toml",
    "role": "examined",
    "excerpt": "filament-specification-qualification = { git = \"https://github.com/agent-ix/filament-specification\", rev = \"ac130b973b1815221cc01a86723f79f0007fd11d\" }"
  },
  {
    "id": "Cargo.lock",
    "path": "Cargo.lock",
    "role": "examined",
    "excerpt": "source = \"git+https://github.com/agent-ix/filament-exact?rev=a58474cc105a86f3307a11def3fc001e2459679f#a58474cc105a86f3307a11def3fc001e2459679f\""
  },
  {
    "id": "measurement/exact-panic/Cargo.toml",
    "path": "measurement/exact-panic/Cargo.toml",
    "role": "examined",
    "excerpt": "test = false\nbench = false"
  },
  {
    "id": "tools/kernel-api-check/Cargo.toml",
    "path": "tools/kernel-api-check/Cargo.toml",
    "role": "examined",
    "excerpt": "filament-exact = { git = \"https://github.com/agent-ix/filament-exact\", rev = \"a58474cc105a86f3307a11def3fc001e2459679f\", default-features = false }"
  },
  {
    "id": "tests/exact_outcome_consumer.rs",
    "path": "tests/exact_outcome_consumer.rs",
    "role": "examined",
    "excerpt": "| ChargePoint::ModelCandidate => {}"
  }
]
```
