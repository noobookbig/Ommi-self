# Ommi.Calc — Pure Utility Math

> **This project contains pure utility math only. No interpretive symbol systems (digit-trait mappings, divinatory mappings, energy-center assignments, period-shape interpretations, or personality typing) live here. Interpretation is performed by specialized agents per project policy MET-394.**

## Scope

`Ommi.Calc` is the deterministic math layer that every forecast in the Ommi self
project depends on. It is intentionally tiny: arithmetic on dates and digits.

### What lives here

- `AgeCalculator` — exact years / months / days between a DOB and a target date.
- `DayOfYear` — day-of-year, day-of-month, day-of-quarter, and period length helpers.
- `PersonalYear` — pure arithmetic reduction of (DOB day + DOB month + DOB year + target year)
  digits to a single digit using standard numerological digit-sum reduction.
- `MatrixReduce` — pure arithmetic: digit sums and row-major matrix index → reduced value.

### What does NOT live here

- Number-to-trait mappings (e.g. "1 = leader", "2 = diplomat", "9 = late bloomer")
- Divinatory card mappings
- Body-center / energy / aura assignments
- Period-shape interpretation (only the date math that frames a period)
- Personality typing
- Any other interpretive mapping

If you need to *interpret* a number, an energy center, a period row, or a
personality type, do that in an agent layer, never in `Ommi.Calc`.

### Reference types

- `PersonDob(DateOnly Dob)`
- `Period(DateOnly Start, DateOnly End)`

These are value records. No business entities, no I/O, no implicit state.

### Purity rules

- No `DateTime.Now`, `DateTime.UtcNow`, or environment access.
- All methods are static and pure: same inputs → same outputs.
- Dates are passed in by the caller.
- No NuGet packages beyond .NET 8 defaults and xUnit (in the test project).

## Build & test

```sh
cd code
dotnet build
dotnet test
```

Both commands exit 0 in CI.

## Layout

```
code/
  Ommi.Calc.sln
  Ommi.Calc/              -- class library (net8.0)
    AgeCalculator.cs
    DayOfYear.cs
    PersonalYear.cs
    MatrixReduce.cs
    PersonDob.cs
    Period.cs
    Ommi.Calc.csproj
  Ommi.Calc.Tests/        -- xUnit tests (net8.0)
    AgeCalculatorTests.cs
    DayOfYearTests.cs
    PersonalYearTests.cs
    MatrixReduceTests.cs
    ReferenceTypesTests.cs
    Ommi.Calc.Tests.csproj
```