using Ommi.Calc;
using Xunit;

namespace Ommi.Calc.Tests;

public class PersonalYearTests
{
    [Fact]
    public void SumDigits_SingleDigit_ReturnsSame()
    {
        Assert.Equal(7, PersonalYear.SumDigits(7));
    }

    [Fact]
    public void SumDigits_MultiDigit_SumsAll()
    {
        Assert.Equal(15, PersonalYear.SumDigits(456));
        Assert.Equal(10, PersonalYear.SumDigits(19));
    }

    [Fact]
    public void SumDigits_Zero_IsZero()
    {
        Assert.Equal(0, PersonalYear.SumDigits(0));
    }

    [Fact]
    public void ReduceToSingleDigit_AlreadySingle_IsSame()
    {
        Assert.Equal(5, PersonalYear.ReduceToSingleDigit(5));
    }

    [Fact]
    public void ReduceToSingleDigit_TwoDigits_OneStep()
    {
        Assert.Equal(9, PersonalYear.ReduceToSingleDigit(18));
        Assert.Equal(7, PersonalYear.ReduceToSingleDigit(25));
    }

    [Fact]
    public void ReduceToSingleDigit_LargeMultiStep()
    {
        Assert.Equal(9, PersonalYear.ReduceToSingleDigit(999));
        Assert.Equal(9, PersonalYear.ReduceToSingleDigit(9999));
    }

    [Fact]
    public void ReduceToSingleDigit_Negative_Throws()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => PersonalYear.ReduceToSingleDigit(-1));
    }

    [Fact]
    public void PersonalYear_KnownValue()
    {
        var dob = new PersonDob(new DateOnly(1990, 5, 15));
        Assert.Equal(4, PersonalYear.Reduce(dob, 2026));
    }

    [Fact]
    public void PersonalYear_AnotherKnownValue()
    {
        var dob = new PersonDob(new DateOnly(1985, 12, 31));
        Assert.Equal(3, PersonalYear.Reduce(dob, 2025));
    }

    [Fact]
    public void PersonalYear_SingleDigitComponents_NoReduction()
    {
        var dob = new PersonDob(new DateOnly(2001, 2, 3));
        Assert.Equal(9, PersonalYear.Reduce(dob, 2026));
    }

    [Fact]
    public void PersonalYear_MasterNumber_Born11_ReducesCorrectly()
    {
        var dob = new PersonDob(new DateOnly(1991, 1, 1));
        Assert.Equal(3, PersonalYear.Reduce(dob, 2024));
    }
}