const validateInput = (input, max_length) => {
  return input && input.length < max_length;
};

const validateName = (name) => {
  return validateInput(name, 200);
};

const validateEmail = (email) => {
  // Simple regex for basic email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return false; // Invalid email format
  }
  return validateInput(email, 100);
};

const validatePhoneNumber = (number) => {
  // Regex for validating chile phone numbers
  const phoneRegex = /^\+?56\s?9\d{8}$/;
  if (!phoneRegex.test(number)) {
    return false; // Invalid phone number format
  }
  return validateInput(number, 100);
};

const validateDate = (date) => {
  // Regex for validating date in YYYY-MM-DD format
  const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
  if (!dateRegex.test(date)) {
    return false; // Invalid date format
  }
  return validateInput(date, 10);
};
