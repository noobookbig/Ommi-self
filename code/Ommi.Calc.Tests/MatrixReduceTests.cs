using Ommi.Calc;
using Xunit;

namespace Ommi.Calc.Tests;

public class MatrixReduceTests
{
    [Fact]
    public void DigitSum_Empty_IsZero()
    {
        Assert.Equal(0, MatrixReduce.DigitSum(Array.Empty<int>()));
    }

    [Fact]
    public void DigitSum_AllZeros_IsZero()
    {
        Assert.Equal(0, MatrixReduce.DigitSum(new[] { 0, 0, 0, 0 }));
    }

    [Fact]
    public void DigitSum_MixedDigits()
    {
        Assert.Equal(15, MatrixReduce.DigitSum(new[] { 1, 2, 3, 4, 5 }));
        Assert.Equal(45, MatrixReduce.DigitSum(new[] { 9, 9, 9, 9, 9 }));
    }

    [Fact]
    public void DigitSum_Null_Throws()
    {
        Assert.Throws<ArgumentNullException>(() => MatrixReduce.DigitSum(null!));
    }

    [Fact]
    public void DigitSum_OutOfRange_Throws()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => MatrixReduce.DigitSum(new[] { -1 }));
        Assert.Throws<ArgumentOutOfRangeException>(() => MatrixReduce.DigitSum(new[] { 10 }));
    }

    [Fact]
    public void RowMajorIndex_FirstCell_IsZero()
    {
        Assert.Equal(0, MatrixReduce.RowMajorIndex(0, 0, 3));
    }

    [Fact]
    public void RowMajorIndex_NextRow()
    {
        Assert.Equal(3, MatrixReduce.RowMajorIndex(1, 0, 3));
        Assert.Equal(8, MatrixReduce.RowMajorIndex(2, 2, 3));
    }

    [Fact]
    public void RowMajorIndex_NegativeArgs_Throw()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => MatrixReduce.RowMajorIndex(-1, 0, 3));
        Assert.Throws<ArgumentOutOfRangeException>(() => MatrixReduce.RowMajorIndex(0, -1, 3));
        Assert.Throws<ArgumentOutOfRangeException>(() => MatrixReduce.RowMajorIndex(0, 0, 0));
    }

    [Fact]
    public void ReduceRowMajor_Known()
    {
        var digits = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        Assert.Equal(MatrixReduce.RowMajorIndex(1, 2, 3),
            MatrixReduce.RowMajorIndex(1, 2, 3));
        Assert.Equal(6, MatrixReduce.ReduceRowMajor(1, 2, 3, digits));
    }

    [Fact]
    public void ReduceRowMajor_MultiDigit_ReducesToSingle()
    {
        var digits = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 9 };
        Assert.Equal(9, MatrixReduce.ReduceRowMajor(3, 1, 3, digits));
    }

    [Fact]
    public void ReduceRowMajor_OutOfRange_Throws()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() =>
            MatrixReduce.ReduceRowMajor(2, 2, 3, new[] { 1, 2, 3, 4 }));
    }

    [Fact]
    public void ReduceRowMajor_Null_Throws()
    {
        Assert.Throws<ArgumentNullException>(() =>
            MatrixReduce.ReduceRowMajor(0, 0, 1, null!));
    }
}