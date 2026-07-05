namespace Ommi.Calc;

/// <summary>
/// Pure utility range type for day-of-period arithmetic. No interpretation.
/// </summary>
public readonly record struct Period(DateOnly Start, DateOnly End);