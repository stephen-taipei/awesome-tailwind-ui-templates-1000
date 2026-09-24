import { test } from 'node:test';
import assert from 'node:assert/strict';
import { digitsOnly, distributeDigits, isCompleteCode } from '../assets/js/otp-core.mjs';
test('OTP formatting accepts ASCII and full-width digits without preserving other text', () => {
  assert.equal(digitsOnly('１２a３ ４-５６'), '123456');
  assert.equal(digitsOnly(null), '');
  assert.equal(digitsOnly('<img onerror=alert()>'), '');
});
test('complete OTP paste replaces all fields even from a later field', () => {
  const original = ['9', '9', '9', '9', '9', '9'];
  assert.deepEqual(distributeDigits(original, 3, '123456'), { values: ['1','2','3','4','5','6'], focus: 5 });
  assert.deepEqual(original, Array(6).fill('9'));
});
test('partial OTP paste starts at the active field and stays in bounds', () => {
  assert.deepEqual(distributeDigits(['1','','',''], 1, '２３'), { values: ['1','2','3',''], focus: 3 });
  assert.deepEqual(distributeDigits(['1','2','3',''], 3, '45'), { values: ['1','2','3','4'], focus: 3 });
  assert.deepEqual(distributeDigits(['1','2'], 1, 'abc'), { values: ['1','2'], focus: 1 });
});
test('OTP helpers reject invalid indices and only validate format, never credentials', () => {
  assert.throws(() => distributeDigits([], 0, '123'), RangeError);
  assert.throws(() => distributeDigits([''], -1, '1'), RangeError);
  assert.equal(isCompleteCode('123456', 6), true);
  for (const value of ['', '12345', '1234567', '12 456', '１２３４５６']) assert.equal(isCompleteCode(value, 6), false);
  assert.equal(isCompleteCode('123', -1), false);
});
