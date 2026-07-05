namespace Ommi.Calc;

/// <summary>
/// Pure reduction utilities for digit sums and row-major matrix index → final value.
/// No interpretation: any meaning attached to the resulting value is the agent's job per
/// project policy MET-394.
/// </summary>
public static class MatrixReduce
{
    public static int DigitSum(IEnumerable<int> values)
    {
        ArgumentNullException.ThrowIfNull(values);
        var sum = 0;
        foreach (var v in values)
        {
            if (v < 0 || v > 9)
            {
                throw new ArgumentOutOfRangeException(nameof(values), "each digit must be 0..9");
            }
            sum += v;
        }
        return sum;
    }

    public static int RowMajorIndex(int row, int column, int columnCount)
    {
        if (row < 0) throw new ArgumentOutOfRangeException(nameof(row));
        if (column < 0) throw new ArgumentOutOfRangeException(nameof(column));
        if (columnCount <= 0) throw new ArgumentOutOfRangeException(nameof(columnCount));
        return (row * columnCount) + column;
    }

    public static int ReduceRowMajor(int row, int column, int columnCount, IEnumerable<int> flatDigits)
    {
        ArgumentNullException.ThrowIfNull(flatDigits);
        var idx = RowMajorIndex(row, column, columnCount);
        var digits = flatDigits.ToArray();
        if (idx < 0 || idx >= digits.Length)
        {
            throw new ArgumentOutOfRangeException(nameof(flatDigits),
                $"index {idx} out of range for digit array of length {digits.Length}");
        }
        return PersonalYear.ReduceToSingleDigit(digits[idx]);
    }
}