---
id: "SR-2026110705000817"
title: "Runtime PR231 coherent SV prerequisite code review"
type: SpecReview
analysis: code-review
scope: "agent-ix/filament-contract-runtime; Cargo.toml, Cargo.lock, measurement/exact-panic/Cargo.toml, tests/exact_outcome_consumer.rs; QSL-2757"
review_set: subset
relationships:
  - target: ix://agent-ix/filament-contract-runtime
    type: references
---

## Summary

Reviewed the four-file prerequisite diff with the code-review Rust lane and mandatory rust-style rules. No new code, API, allocator, safety, gate-integrity, or dependency-identity defect was found.

Ticket: QSL-2757 (ARCH-assigned prerequisite; ticket remains open until the driver and four staged CLI cases pass). PR: filament-contract-runtime#231. Frozen head: `d00f1183825e9ff3707aab5c658c84cf161159fd`. Base: `75688ead74e265bcb654de871577570b7b15e19c`.

Review-only execution: no source edits, Cargo invocations, tests, builds, measurements, proof runs, feature sweeps, old-head runs, or fresh baselines. `git diff --check` and direct `rustfmt --check --edition 2021 tests/exact_outcome_consumer.rs` passed. Installed tools on terra: `/home/peter/.npm-global/bin/quire` 0.52.0 (engine 0.62.2), `/home/peter/.npm-global/bin/quoin` 0.36.8; versions differ from the supplied release notice and were reported to the lead. Active schema: spec-artifacts-process@v0.36.0.

## Verdict

**PASS** for this frozen diff's static code/Rust review. Mergeable on source review, subject to the lead's final exact-head gates and disposition of inherited assurance limitations in the separate gap artifact. This is not a repository-wide assurance or test-execution claim.

## Findings

| ID | Severity | Summary | Refs |
| --- | --- | --- | --- |
| FND-001 | low | No findings (placeholder) | - |

## Review Evidence

All normal, dev failing-allocator, and measurement SV dependencies select `fa5e78aa71fcea5418492b67f13a33124af84459`; the lock contains one SV and one failing-allocator entry at that source. Exactly one `filament-exact` lock entry remains at `b26a8e4c592503fccdc4a0e3d2cce23dd8487616`, matching the adopted SV manifest's exact dependency. The two quire-canonical packages each have one lock entry. No IR, model, evaluation leaf, or observation dependency is added. Optional exact features and default-features settings are unchanged. No production source, CI, profile, allocator, target selection, or panic handler changes.

The sole Rust edit adds the explicit `Undefined::MalformedNumber` arm to the exhaustive consumer match. The unchanged exact owner defines it at `src/outcome.rs:118-120` as malformed text-to-number input (FSpec `malformed-number`). The helper remains a compile-time vocabulary guard, with no catch-all or alternate value mapping. Existing traced consumer assertions distinguish completed false/true from Undefined, Refused, and Incomplete and execute the real lazy Boolean runtime seam. This arm is not claimed as a new malformed-number execution test.

The measurement target is a `no_std` static library containing zero test functions, bench functions, or cfg(test) sections. `test = false` and `bench = false` express that actual target and remove no real test or assertion. Makefile:118 builds the archive with the manifest MSRV 1.98.1, profile `exact-panic`, and `thumbv7em-none-eabi`. Its refusing allocator and panic handler are both cfg(target_os = "none"); the intended target is essential. This change does not weaken the archive build, retained-call population, or panic-relocation inspection. No native host test claim is made.

The diff adds no copied implementation, vocabulary definition, wrapper, fallback mapping, coverage threshold change, warning suppression, or new unsafe operation. No applicable AssuranceProfile exists in spec/. Repository AGENTS/CLAUDE, CONTRIBUTING, clippy, deny, rustfmt, and manifest rules were read.

## Inherited Policy and Evidence

FR-275-AC-4 states branch = main with no rev. Both reviewed manifests already used rev pins at the supplied base. The lead relayed ARCH's explicit instruction to adopt exactly SV fa5e78aa and leave exact b26 unchanged for this bounded coherent wave; that directive governs this change. This review does not claim AC-4 conformance or amend it. The retained function-application port and unmet FR-275 end state are unchanged and outside this prerequisite.

Execution evidence supplied by the lead: at 3f62, exact root library 8 PASS and three integration targets 33 PASS; at e7db, exact_outcome_consumer 2 PASS, total 43 actual PASS, 0 fail, 0 ignore. At the frozen d00 head, the proper cross-target all-target check and documented build exited 0 after only measurement test/bench metadata changed. These are attributed reports, not reviewer reruns. Compiler checks and builds contribute zero tests to that count. The lead retains ownership of the final rebased runtime and adopted-FSL exact-head gates before merge.

## Examined Scope

```json
[
  {
    "id": "Cargo.toml",
    "path": "Cargo.toml",
    "role": "examined",
    "excerpt": "exact = [\"alloc\", \"dep:filament-exact\", \"dep:filament-semantic-value\"]"
  },
  {
    "id": "Cargo.lock",
    "path": "Cargo.lock",
    "role": "examined",
    "excerpt": "name = \"filament-semantic-value\""
  },
  {
    "id": "measurement/exact-panic/Cargo.toml",
    "path": "measurement/exact-panic/Cargo.toml",
    "role": "examined",
    "excerpt": "crate-type = [\"staticlib\"]\ntest = false\nbench = false"
  },
  {
    "id": "tests/exact_outcome_consumer.rs",
    "path": "tests/exact_outcome_consumer.rs",
    "role": "examined",
    "excerpt": "        | Undefined::MalformedNumber => {}"
  },
  {
    "id": "FR-006-AC-1",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "The four outcome dispositions are distinct; completed `false` is a value. `Refusal` and `Undefined` are closed enums; `Incomplete` is a typed record whose reason uses the closed `LimitKind` and `ChargePoint` enums. The runtime consumes these kernel types directly under FR-275."
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
  }
]
```
