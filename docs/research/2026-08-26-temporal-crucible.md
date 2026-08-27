# Temporal Crucible — controlled ignorance across time

**Status:** CANDIDATE METHOD · RESEARCH NOTE · NO PROMOTION

**Date:** 2026-08-26

## Trigger

Two nearby artifacts exposed the same epistemic shape from opposite temporal directions.

1. ALEX's newly merged Blind Crucible lowers a canonical specimen into **CASE** and **ORACLE**, then exposes only CASE to the runtime. ORACLE stays harness-side until scoring. The boundary exists to prevent answer-key dependence while preserving expected outcomes as historical authoring material.
2. The Daily Slice's sealed **SLICING AHEAD** experiment freezes a forward structural prediction before the date it names, explicitly refusing later widening or target movement. Its proposed `NEXT-STEP-HOLDOUT-001` asks whether frozen historical cuts can predict later transformation classes better than ugly controls.

These are not independent discoveries. They share project ancestry and current collaborators. The useful relation is architectural, not evidentiary corroboration.

## Candidate relation

```text
BLIND CRUCIBLE
CASE -----------> RUNTIME
                  |
ORACLE withheld  | result
                  v
              SCORE LATER

TEMPORAL CRUCIBLE
PAST -----------> FORECAST
                  |
FUTURE withheld  | claim
                  v
              SCORE LATER
```

The common primitive is **controlled ignorance**:

> A claim earns stronger evidentiary weight when the information that could trivially determine or retrofit its answer is unavailable at claim-formation time, while the later scoring rule remains attributable.

This does **not** mean blindness is sufficient for truth. A blind test can still be badly designed, vague, underpowered, selectively interpreted, or scored by a moving rule.

## External pressure

### Preregistration

Preregistration archives hypotheses, design, procedure, and/or analysis plans before outcomes are known so later readers can distinguish prediction from postdiction and inspect deviations. It can reduce HARKing and selective reporting, but it is neither sufficient nor universally necessary for good science; vague or arbitrary registrations can simply freeze a bad plan.

Relevant sources:

- Pham & Oh (2020), *Preregistration Is Neither Sufficient nor Necessary for Good Science*. DOI: https://doi.org/10.1002/jcpy.1209
- Parker, Fraser & Nakagawa (2019), on preregistration and registered reports in conservation science. DOI: https://doi.org/10.1111/cobi.13342
- Chambers & Tzavella (2022), review of Registered Reports. DOI: https://doi.org/10.1038/s41562-021-01193-7

The strongest import for ALEX is not “always preregister.” It is:

```text
planned claim
!=
post-hoc explanation
```

and deviations should survive as deviations rather than being rewritten into the original plan.

### Prequential evaluation

Dawid's prequential approach evaluates a forecasting system through predictions issued using only information available up to time `t`, then scores those predictions against outcomes that arrive later. Model merit is therefore tied to sequential predictive performance on unseen observations rather than retrospective fit alone.

Relevant sources:

- Dawid (1984), *The Prequential Approach*. DOI: https://doi.org/10.2307/2981683
- Clarke & Clarke (2009), prequential analysis of complex data. DOI: https://doi.org/10.1002/sam.10052
- Shiffrin et al. (2008), survey of model evaluation including prequential prediction error. DOI: https://doi.org/10.1080/03640210802414826

This looks unusually close to the intended `NEXT-STEP-HOLDOUT-001` shape.

### Proper forecast scoring

Forecast evaluation literature separates calibration from resolution/refinement and recommends proper scoring rules where probabilistic forecasts are involved. A forecaster that says `0.5` to everything can be calibrated in some environments while being informationally useless; scoring must therefore reward useful discrimination, not only eventual compatibility.

Relevant sources:

- Simonis, White & Ernest (2021), probabilistic ecological forecast evaluation. DOI: https://doi.org/10.1002/ecy.3431
- Foster & Hart (2023), calibration versus Brier-score expertise. DOI: https://doi.org/10.3982/TE5330
- Nane & Cooke (2024), scoring rules and expert judgment. DOI: https://doi.org/10.1002/ffo2.189

For qualitative structural forecasts, no off-the-shelf Brier score solves the semantic problem. The event vocabulary and match rule must first be frozen.

### Cryptographic commitments

A hash commitment can commit to a value without revealing it, then allow later verification when the value and blinding material are revealed. The useful analogy is limited but precise: a prediction receipt can bind the exact pre-outcome claim and scoring contract so later edits are detectable.

NIST Crypto Club slides describe the basic commit/reveal pattern: https://csrc.nist.gov/csrc/media/Presentations/2024/crclub-2024-01-24/images-media/20240124-crypto-club--tommaso-marco-sylvain--slides--crypto-audit.pdf

A normal Git commit already supplies much of the practical historical binding needed here. No claim of cryptographic secrecy is required.

## `TEMPORAL-CRUCIBLE-001`

A bounded specimen for structural project forecasts.

### 1. Freeze the CASE

At time `T0`, preserve:

```json
{
  "case_id": "...",
  "cutoff": "T0",
  "visible_sources": ["immutable refs"],
  "forecast": [
    {
      "event_class": "...",
      "probability": 0.0,
      "positive_criteria": ["..."],
      "near_miss_criteria": ["..."],
      "explicit_nonmatches": ["..."]
    }
  ],
  "horizon": "...",
  "controls": ["..."],
  "scoring_contract": "versioned ref"
}
```

The `visible_sources` list matters. A timestamped prediction is weak evidence if its author had already seen the supposedly withheld future through another channel.

### 2. Freeze the vocabulary

Before outcomes arrive, define a small event-class vocabulary. For the current `SLICING AHEAD` hypothesis this might include:

- `REENTRY_TYPED_RELATION`
- `HUMAN_ADMISSION_EXPLICIT`
- `FORMATION_HISTORY_EXPOSED`
- `GLOBAL_MEMORY_AGGREGATION`
- `SEARCH_ONLY_RETRIEVAL`
- `NO_MATERIAL_TRANSFORMATION`

Do not add a new event class merely because tomorrow produced something hard to score. Unclassifiable outcomes must be allowed to remain `UNRESOLVED`.

### 3. Forecast probabilistically

Avoid one giant sentence whose elasticity makes every future count.

Example:

```text
P(REENTRY_TYPED_RELATION within horizon) = 0.60
P(HUMAN_ADMISSION_EXPLICIT)             = 0.55
P(GLOBAL_MEMORY_AGGREGATION)            = 0.15
P(NO_MATERIAL_TRANSFORMATION)           = 0.25
```

These probabilities are candidate inputs, not present claims about the project.

### 4. Preserve ugly controls

Score the actual forecast against alternatives such as:

- recurrence-count baseline;
- keyword-similarity baseline;
- project-frequency baseline;
- shuffled chronology;
- generic “the system will add memory” forecast;
- random plausible next-move forecast;
- ablation of one supposedly load-bearing source family.

A forecast is interesting only if chronology and structure outperform cheap generic stories.

### 5. Let FUTURE become ORACLE carefully

Unlike a normal Crucible fixture, the future does not arrive as a pre-authored answer key. It arrives as evidence.

Therefore ORACLE formation must itself be witnessed:

```text
future evidence
  -> bounded source set
  -> independent classification where practical
  -> disagreements preserved
  -> event-class disposition
  -> score
```

The evaluator must not silently turn a later interpretation into “what happened.”

Suggested dispositions:

- `MATCH`
- `PARTIAL`
- `NONMATCH`
- `UNRESOLVED`
- `CONTAMINATED`

`CONTAMINATED` is essential when the supposed future outcome was materially influenced by seeing the prediction. The forecast may have become an intervention.

### 6. Score specificity, not merely resemblance

A useful forecast should pay for breadth.

Candidate qualitative decomposition:

```text
FORECAST VALUE
  = directional accuracy
  + specificity / resolution
  + calibration across repeated forecasts
  - false-fit cost
  - post-hoc amendment cost
  - contamination cost
```

Do not pretend this is already a mathematically proper scoring rule. The immediate goal is a versioned, falsifiable rubric that can later be formalized.

## The intervention problem

This is the sharpest unresolved issue.

The Daily Slice prediction is public. Project participants can read it. Therefore:

```text
FORECAST
may alter
FUTURE
```

That does not make the experiment useless, but it changes what is being tested.

There are at least three distinct claims:

1. **Predictive:** the frozen past anticipated later work that would have happened anyway.
2. **Constitutive:** articulating the pressure helped the group choose a later move.
3. **Constraint-revealing:** the prediction and later work share an upstream structural cause, so publishing the prediction changed timing or vocabulary but not the deeper directional pressure.

`TEMPORAL-CRUCIBLE-001` must not collapse these.

A stronger future test can use an embargoed or hash-committed forecast whose content is revealed only after the horizon closes. That trades immediate usefulness for cleaner causal interpretation.

## Candidate law

> **Blindness is not absence of evidence. It is an information boundary that preserves which evidence was available when a claim was formed.**

And the temporal version:

> **A future prediction becomes a stronger witness when both the claim and its scoring grammar are bound before the future can answer back.**

## Failure conditions

Kill or downgrade the method if:

- event classes expand after outcomes arrive;
- every later move can be scored as a partial match;
- the forecast does not beat generic controls;
- evaluator disagreement is hidden;
- future participants knowingly implement the prediction but the result is reported as pure prediction;
- source cutoffs leak later summaries;
- probabilities or criteria are silently edited;
- too few forecasts accumulate to evaluate calibration meaningfully.

## Next bounded move

Do **not** turn this into a forecasting platform.

Run three historical backtests first using frozen repository cuts, then one genuinely prospective specimen with a short horizon. Preserve failures.

If that works, ALEX may have discovered a reusable sibling of the Blind Crucible:

```text
SPATIAL BLINDNESS: runtime cannot see ORACLE
TEMPORAL BLINDNESS: predictor cannot see FUTURE

both preserve
FORMATION CONDITIONS OF A CLAIM
```

That is the research candidate. Not canon.