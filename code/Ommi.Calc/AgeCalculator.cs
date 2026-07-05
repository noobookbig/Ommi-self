namespace Ommi.Calc;

/// <summary>
/// Exact years/months/days elapsed between two dates. Pure arithmetic; no interpretation.
/// Uses DateOnly.AddYears/AddMonths which handle leap-year clamping deterministically
/// (e.g. Feb 29 + 1 year in a non-leap year → Feb 28).
/// </summary>
public readonly record struct AgeResult(int Years, int Months, int Days);

public static class AgeCalculator
{
    public static AgeResult Calculate(PersonDob dob, DateOnly target)
    {
        if (target < dob.Dob)
        {
            throw new ArgumentException("target must be on or after dob", nameof(target));
        }

        var years = target.Year - dob.Dob.Year;
        var anchorYears = dob.Dob.AddYears(years);
        if (anchorYears > target)
        {
            years -= 1;
            anchorYears = dob.Dob.AddYears(years);
        }

        var months = 0;
        while (months < 12 && anchorYears.AddMonths(months + 1) <= target)
        {
            months += 1;
        }

        var anchorMonths = anchorYears.AddMonths(months);
        var days = target.DayNumber - anchorMonths.DayNumber;

        return new AgeResult(years, months, days);
    }
}