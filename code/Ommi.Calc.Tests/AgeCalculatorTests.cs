using Ommi.Calc;
using Xunit;

namespace Ommi.Calc.Tests;

public class AgeCalculatorTests
{
    [Fact]
    public void SameDay_IsZero()
    {
        var dob = new PersonDob(new DateOnly(1990, 5, 15));
        var age = AgeCalculator.Calculate(dob, new DateOnly(1990, 5, 15));
        Assert.Equal(new AgeResult(0, 0, 0), age);
    }

    [Fact]
    public void ExactYears()
    {
        var dob = new PersonDob(new DateOnly(1990, 5, 15));
        var age = AgeCalculator.Calculate(dob, new DateOnly(2020, 5, 15));
        Assert.Equal(new AgeResult(30, 0, 0), age);
    }

    [Fact]
    public void DayBeforeBirthday_BorrowsMonthAndYear()
    {
        var dob = new PersonDob(new DateOnly(1990, 5, 15));
        var age = AgeCalculator.Calculate(dob, new DateOnly(2020, 5, 14));
        Assert.Equal(new AgeResult(29, 11, 29), age);
    }

    [Fact]
    public void MonthsBorrowing()
    {
        var dob = new PersonDob(new DateOnly(1990, 5, 15));
        var age = AgeCalculator.Calculate(dob, new DateOnly(2020, 3, 20));
        Assert.Equal(new AgeResult(29, 10, 5), age);
    }

    [Fact]
    public void LeapYearDob_Feb29ToMar1_NonLeapYear()
    {
        var dob = new PersonDob(new DateOnly(2000, 2, 29));
        var age = AgeCalculator.Calculate(dob, new DateOnly(2021, 3, 1));
        Assert.Equal(new AgeResult(21, 0, 1), age);
    }

    [Fact]
    public void TargetBeforeDob_Throws()
    {
        var dob = new PersonDob(new DateOnly(2000, 1, 1));
        Assert.Throws<ArgumentException>(() =>
            AgeCalculator.Calculate(dob, new DateOnly(1999, 12, 31)));
    }
}