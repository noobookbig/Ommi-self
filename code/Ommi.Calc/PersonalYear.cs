namespace Ommi.Calc;

/// <summary>
/// Pure arithmetic reduction of DOB digits plus a target year to a single digit
/// using standard numerological digit-sum reduction. Each component (day, month,
/// year of birth and the target year) is first reduced to a single digit, then
/// the four single digits are summed and reduced again. The meaning/interpretation
/// of the resulting digit is performed by specialized agents per project policy
/// MET-394 and is intentionally NOT implemented here.
/// </summary>
public static class PersonalYear
{
    public static int Reduce(PersonDob dob, int targetYear)
    {
        var dayDigit = ReduceToSingleDigit(dob.Dob.Day);
        var monthDigit = ReduceToSingleDigit(dob.Dob.Month);
        var yearDigit = ReduceToSingleDigit(dob.Dob.Year);
        var targetDigit = ReduceToSingleDigit(targetYear);
        var combined = dayDigit + monthDigit + yearDigit + targetDigit;
        return ReduceToSingleDigit(combined);
    }

    public static int ReduceToSingleDigit(int value)
    {
        if (value < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(value), "value must be non-negative");
        }
        var current = value;
        while (current >= 10)
        {
            current = SumDigits(current);
        }
        return current;
    }

    public static int SumDigits(int value)
    {
        if (value < 0)
        {
            throw new ArgumentOutOfRangeException(nameof(value), "value must be non-negative");
        }
        var sum = 0;
        var n = value;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}