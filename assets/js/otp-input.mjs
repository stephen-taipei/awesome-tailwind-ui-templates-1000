import { digitsOnly, distributeDigits, isCompleteCode } from './otp-core.mjs';

/** Opt-in, frontend-only OTP demo. These controls do not authenticate anyone. */
export function setupOtpGroup(group) {
  if (group.dataset.otpReady) return;
  const inputs = [...group.querySelectorAll('input')];
  if (!inputs.length || inputs.some(input => input.type !== 'text')) return;
  const single = inputs.length === 1;
  const length = single ? inputs[0].maxLength : inputs.length;
  if (!Number.isInteger(length) || length < 1 || length > 12) return;
  group.dataset.otpReady = 'true';
  group.dir = 'ltr';
  const status = document.createElement('p');
  status.dataset.otpStatus = '';
  status.setAttribute('role', 'status');
  status.className = 'mt-3 text-sm';
  group.after(status);

  const clearError = () => {
    for (const input of inputs) input.removeAttribute('aria-invalid');
    status.textContent = '';
  };
  const focus = index => { inputs[index].focus(); inputs[index].select(); };
  const apply = (index, text) => {
    clearError();
    const digits = digitsOnly(text);
    if (single) {
      inputs[0].value = digits.slice(0, length);
      return;
    }
    if (!digits) { inputs[index].value = ''; return; }
    const next = distributeDigits(inputs.map(input => input.value), index, digits);
    next.values.forEach((value, i) => { inputs[i].value = value; });
    focus(next.focus);
  };
  inputs.forEach((input, index) => {
    input.addEventListener('input', event => {
      if (!event.isComposing) apply(index, event.data?.length > 1 ? event.data : input.value);
    });
    input.addEventListener('compositionend', event => apply(index, event.data || input.value));
    // beforeinput preserves a whole autofill payload before maxlength truncates it.
    input.addEventListener('beforeinput', event => {
      if (event.isComposing || !event.data || !event.inputType.startsWith('insert')) return;
      if (!single && event.data.length > 1) { event.preventDefault(); apply(index, event.data); }
    });
    input.addEventListener('paste', event => {
      if (!event.clipboardData) return;
      event.preventDefault();
      apply(index, event.clipboardData.getData('text'));
    });
    input.addEventListener('keydown', event => {
      if (single || event.altKey || event.ctrlKey || event.metaKey || event.isComposing) return;
      if (event.key === 'ArrowLeft' && index > 0) { event.preventDefault(); focus(index - 1); }
      if (event.key === 'ArrowRight' && index < inputs.length - 1) { event.preventDefault(); focus(index + 1); }
      if (event.key === 'Backspace' && !input.value && index > 0) {
        event.preventDefault(); clearError(); inputs[index - 1].value = ''; focus(index - 1);
      }
    });
  });
  const verifyFormat = event => {
    event.preventDefault();
    const code = inputs.map(input => input.value).join('');
    const valid = isCompleteCode(code, length) && (single || inputs.every(input => input.value.length === 1));
    if (!valid) {
      const invalid = inputs.find(input => !isCompleteCode(input.value, single ? length : 1)) || inputs[0];
      invalid.setAttribute('aria-invalid', 'true');
      status.textContent = `Enter all ${length} digits. This is a frontend demo.`;
      invalid.focus();
      return;
    }
    for (const input of inputs) input.removeAttribute('aria-invalid');
    status.textContent = 'Code format is complete. Demo only: no information was submitted and no authentication was performed.';
  };
  const form = group.closest('form');
  if (form) {
    // The group is an explicit demo opt-in. Avoid native validation skipping our status.
    form.noValidate = true;
    form.addEventListener('submit', verifyFormat);
    form.addEventListener('reset', clearError);
  } else {
    group.closest('[role="dialog"]')?.querySelector('[data-otp-verify]')?.addEventListener('click', verifyFormat);
  }
}
for (const group of document.querySelectorAll('[data-otp-group]')) setupOtpGroup(group);
