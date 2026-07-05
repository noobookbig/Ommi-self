using Ommi.Calc;
using Xunit;

namespace Ommi.Calc.Tests;

public class ReferenceTypesTests
{
    [Fact]
    public void PersonDob_Equality()
    {
        var a = new PersonDob(new DateOnly(2000, 1, 1));
        var b = new PersonDob(new DateOnly(2000, 1, 1));
        var c = new PersonDob(new DateOnly(2000, 1, 2));
        Assert.Equal(a, b);
        Assert.NotEqual(a, c);
    }

    [Fact]
    public void Period_Equality()
    {
        var a = new Period(new DateOnly(2020, 1, 1), new DateOnly(2020, 12, 31));
        var b = new Period(new DateOnly(2020, 1, 1), new DateOnly(2020, 12, 31));
        var c = new Period(new DateOnly(2020, 1, 1), new DateOnly(2020, 12, 30));
        Assert.Equal(a, b);
        Assert.NotEqual(a, c);
    }
}