/** Pure formatting only. Never verifies, persists or submits a security code. */
export function digitsOnly(value) {
  return String(value ?? '').normalize('NFKC').replace(/[^0-9]/g, '');
}

/** Distribute a paste/autofill payload without mutating the caller's values. */
export function distributeDigits(values, start, text) {
  if (!Array.isArray(values) || !values.length || !Number.isInteger(start) || start < 0 || start >= values.length) {
    throw new RangeError('A valid field index and nonempty values are required');
  }
  const digits = digitsOnly(text);
  const next = values.slice();
  // A complete code pasted into any cell replaces the whole code.
  const offset = digits.length >= values.length ? 0 : start;
  for (let i = 0; i < Math.min(digits.length, next.length - offset); i++) next[offset + i] = digits[i];
  return { values: next, focus: digits.length ? Math.min(offset + digits.length, next.length - 1) : start };
}

export function isCompleteCode(value, length) {
  return Number.isInteger(length) && length > 0 && new RegExp(`^[0-9]{${length}}$`).test(value);
}
