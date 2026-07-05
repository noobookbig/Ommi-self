namespace Ommi.Calc;

/// <summary>
/// Day-of-period arithmetic: how many days into the year/month/quarter a date falls,
/// and total length of those periods. Pure arithmetic; no interpretation.
/// </summary>
public static class DayOfYear
{
    public static int DayOfGregorianYear(DateOnly date)
        => date.DayNumber - new DateOnly(date.Year, 1, 1).DayNumber + 1;

    public static int DaysInYear(int year)
        => DateTime.IsLeapYear(year) ? 366 : 365;

    public static int DayOfMonth(DateOnly date) => date.Day;

    public static int DaysInMonth(DateOnly date) => DateTime.DaysInMonth(date.Year, date.Month);

    public static int DayOfQuarter(DateOnly date)
    {
        var quarterStartMonth = ((date.Month - 1) / 3) * 3 + 1;
        var quarterStart = new DateOnly(date.Year, quarterStartMonth, 1);
        return date.DayNumber - quarterStart.DayNumber + 1;
    }

    public static int DaysInQuarter(int year, int quarter)
    {
        if (quarter < 1 || quarter > 4)
        {
            throw new ArgumentOutOfRangeException(nameof(quarter), "quarter must be 1..4");
        }
        var startMonth = (quarter - 1) * 3 + 1;
        return DateTime.DaysInMonth(year, startMonth)
             + DateTime.DaysInMonth(year, startMonth + 1)
             + DateTime.DaysInMonth(year, startMonth + 2);
    }
}