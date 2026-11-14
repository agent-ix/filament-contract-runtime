# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Agent-IX
"""filament-contract-runtime's documentation figures, rendered by the docs-figures skill.

Regenerate from the repository root with the agent-ix/dev-tools skill:

    python3 -m pip install fonttools
    python3 <dev-tools>/skills/docs-figures/scripts/render.py docs/images/figures.py

Add --check to confirm the committed SVGs are current.
"""

from docs_figures import FONTS, SMALL, TITLE, Figure  # noqa: F401

STYLE = "ix-docs"

# One role per kind of thing, fixed across the Filament repositories.
ROLES = [
    ("code", "authored source", "box"),
    ("logic", "compiler stage", "box"),
    ("model", "checked package / IR", "box"),
    ("evidence", "outcome", "box"),
    ("ink", "input", "box"),
]


def hero():
    """README hero: a generated oracle calls the runtime and gets one of three verdicts."""
    f = Figure(
        "hero",
        1040,
        350,
        "A generated oracle passes observed values to filament-contract-runtime, which returns one "
        "of three verdicts: Passed, FailedPostcondition or RejectedPrecondition. A campaign report "
        "counts every verdict.",
    )
    f.box(0, 100, 160, 56, "ink", "observed values", "inputs and results")
    f.box(210, 100, 250, 56, "model", "generated oracle", "from filament-contract-codegen")
    f.box(510, 100, 220, 56, "logic", "filament-contract-runtime", "checked ops · clauses")
    f.line([(160, 128), (207, 128)], "ink")
    f.line([(460, 128), (507, 128)], "model")
    trunk = 758
    f.line([(730, 128), (trunk, 128)], "logic", arrow=False)
    f.line([(trunk, 28), (trunk, 180)], "logic", arrow=False)
    verdicts = [
        (0, "Passed", "all required clauses held"),
        (76, "FailedPostcondition", "accepted, postcondition false"),
        (152, "RejectedPrecondition", "case outside the input domain"),
    ]
    for y, name, sub in verdicts:
        f.line([(trunk, y + 28), (777, y + 28)], "logic")
        f.box(780, y, 260, 56, "evidence", name, sub)
    f.line([(910, 208), (910, 257)], "evidence")
    f.note(898, 238, "each verdict is recorded", "muted", anchor="end")
    f.box(780, 260, 260, 56, "model", "CampaignReport", "four saturating counts")
    f.text(510, 190, "no conversion to bool", "muted", "mono", SMALL)
    f.legend(0, 334, [ROLES[0], ROLES[1], ROLES[2], ("evidence", "verdict", "box"), ROLES[4]])
    return f


REPOS = [
    (1, 0, "filament-driver", "the fsl command", False),
    (2, 0, "filament-integration", "tests the whole chain", False),
    (3, 0, "filament-verification", "plans verification", False),
    (0, 1, "filament-specification", "the standard", False),
    (1, 1, "filament-spec-language", "compiler · evaluator", False),
    (2, 1, "filament-contract-ir", "contract model", False),
    (3, 1, "filament-contract-codegen", "code · tests · proofs", False),
    (4, 1, "filament-contract-runtime", "runs generated checks", False),
    (0, 2, "filament-observation", "qualified observations", False),
    (1, 2, "filament-protocol", "protocol conformance", False),
    (2, 2, "filament-analyze", "SMT consistency", False),
    (0, 3, "filament-mltl", "MLTL over observations", False),
]
FEEDS = [
    ("filament-specification", "filament-spec-language"),
    ("filament-spec-language", "filament-contract-ir"),
    ("filament-contract-ir", "filament-contract-codegen"),
    ("filament-contract-codegen", "filament-contract-runtime"),
    ("filament-spec-language", "filament-protocol"),
    ("filament-contract-ir", "filament-analyze"),
    ("filament-observation", "filament-protocol"),
    ("filament-observation", "filament-mltl"),
]
SHARED = ["filament-eval", "filament-exact", "filament-semantic-value", "filament-walk", "quire-canonical",
          "filament-verification-contracts"]


def ecosystem(here="filament-spec-language"):
    """The Filament repositories: the main chain, its branches, and what runs and shares it."""
    f = Figure(
        "ecosystem",
        980,
        476,
        "The Filament repositories. The main chain runs from the standard, filament-specification, to "
        "the compiler, filament-spec-language, then filament-contract-ir, filament-contract-codegen and "
        "filament-contract-runtime. filament-spec-language also feeds filament-protocol, and "
        "filament-contract-ir feeds filament-analyze. filament-observation feeds filament-protocol and "
        "filament-mltl. Above the chain, filament-driver runs it, filament-integration tests it and "
        "filament-verification plans verification. Below it, shared libraries used throughout: "
        "filament-eval, filament-exact, filament-semantic-value, filament-walk, quire-canonical and "
        "filament-verification-contracts.",
    )
    w, h, step = 176, 50, 201
    rows = {0: 20, 1: 120, 2: 210, 3: 290}
    where = {}
    for col, row, name, sub, _ in REPOS:
        x, y = col * step, rows[row]
        where[name] = (x, y)
        role = "logic" if name == here else "ink"
        f.box(x, y, w, h, role, name, sub)
    for a, b in FEEDS:
        (ax, ay), (bx, by) = where[a], where[b]
        if ay == by:
            f.line([(ax + w, ay + h / 2), (bx - 3, by + h / 2)], "model")
        else:
            f.line([(ax + w / 2, ay + h), (bx + w / 2, by - 3)], "model")
    f.text(0, 12, "ORCHESTRATION", "muted", "mono", SMALL)
    f.text(0, 112, "THE CHAIN", "muted", "mono", SMALL)
    f.text(0, 382, "SHARED LIBRARIES · USED THROUGHOUT", "muted", "mono", SMALL)
    gap = 10
    widths = [FONTS["title"].width(name, TITLE) + 24 for name in SHARED]
    spare = (980 - sum(widths) - gap * (len(SHARED) - 1)) / len(SHARED)
    x = 0
    for name, w0 in zip(SHARED, widths):
        w0 = round(w0 + spare)
        f.box(x, 390, w0, h, "logic" if name == here else "ink", name)
        x += w0 + gap
    f.legend(0, 472, [("logic", "this repository", "box"), ("model", "feeds", "fill")])
    return f


def ecosystem_here():
    """This repository's highlighted copy of the ecosystem figure."""
    return ecosystem(here="filament-contract-runtime")


FIGURES = [hero, ecosystem_here]
