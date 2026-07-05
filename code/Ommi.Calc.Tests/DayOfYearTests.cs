using Ommi.Calc;
using Xunit;

namespace Ommi.Calc.Tests;

public class DayOfYearTests
{
    [Fact]
    public void Jan1_IsOne()
    {
        Assert.Equal(1, DayOfYear.DayOfGregorianYear(new DateOnly(2026, 1, 1)));
    }

    [Fact]
    public void Dec31_NonLeap_Is365()
    {
        Assert.Equal(365, DayOfYear.DayOfGregorianYear(new DateOnly(2025, 12, 31)));
    }

    [Fact]
    public void Dec31_Leap_Is366()
    {
        Assert.Equal(366, DayOfYear.DayOfGregorianYear(new DateOnly(2024, 12, 31)));
    }

    [Fact]
    public void Feb29_Leap_Is60()
    {
        Assert.Equal(60, DayOfYear.DayOfGregorianYear(new DateOnly(2024, 2, 29)));
    }

    [Fact]
    public void DaysInYear_LeapVsNonLeap()
    {
        Assert.Equal(366, DayOfYear.DaysInYear(2024));
        Assert.Equal(365, DayOfYear.DaysInYear(2025));
    }

    [Fact]
    public void QuarterBoundaries()
    {
        Assert.Equal(1, DayOfYear.DayOfQuarter(new DateOnly(2026, 1, 1)));
        Assert.Equal(1, DayOfYear.DayOfQuarter(new DateOnly(2026, 4, 1)));
        Assert.Equal(1, DayOfYear.DayOfQuarter(new DateOnly(2026, 7, 1)));
        Assert.Equal(1, DayOfYear.DayOfQuarter(new DateOnly(2026, 10, 1)));
        Assert.Equal(31, DayOfYear.DayOfQuarter(new DateOnly(2026, 1, 31)));
        Assert.Equal(90, DayOfYear.DayOfQuarter(new DateOnly(2026, 3, 31)));
    }

    [Fact]
    public void DaysInQuarter_Q1_NonLeap_Is90()
    {
        Assert.Equal(90, DayOfYear.DaysInQuarter(2025, 1));
    }

    [Fact]
    public void DaysInQuarter_Q2_NonLeap_Is91()
    {
        Assert.Equal(91, DayOfYear.DaysInQuarter(2025, 2));
    }

    [Fact]
    public void DaysInQuarter_Q1_Leap_Is91()
    {
        Assert.Equal(91, DayOfYear.DaysInQuarter(2024, 1));
    }

    [Fact]
    public void DaysInQuarter_OutOfRange_Throws()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => DayOfYear.DaysInQuarter(2026, 0));
        Assert.Throws<ArgumentOutOfRangeException>(() => DayOfYear.DaysInQuarter(2026, 5));
    }
}