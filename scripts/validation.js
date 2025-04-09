const validateLenght = (input, max_length) => {
  return input.length < max_length;
};

const validateRegion = (regionId) => {
  foundRegion = region_comunas.regiones.find(
    (region) =>  region.numero == regionId
  );
  return (foundRegion != undefined);
}

const validateCommune = (regionId, communeId) => {
  foundRegion = region_comunas.regiones.find((region) => {
    return region.numero == regionId;
  });
  foundCommune = foundRegion.comunas.find(
    (comunne) => comunne.id == communeId);

  return (foundCommune != undefined);
}

const validateSector = (sector) => {
  const sectorRegex = /^[A-Z]{2}$/;
  return validateLenght(sector, 2) && sectorRegex.test(sector);
}

const validateName = (name) => {
  return validateLenght(name, 200);
};

const validateEmail = (email) => {
  const emailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  return validateLenght(email, 100) && emailRegex.test(email);
};

const validatePhoneNumber = (number) => {
  const phoneRegex = /^\+\d{3}\.\d{8}$/;
  return (validateLenght(number, 14) && phoneRegex.test(number));
};

const validateContact = (contact) => {
  const contactRegex = /^[A-Za-z0-9\s]+$/;
  return validateLenght(contact, );
};

const validateDate = (date) => {
  // Regex for validating date in YYYY-MM-DD hh:mmformat
  const dateRegex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/;
  return validateLenght(date, 10) && dateRegex.test(date);
};

const validateEndDate = (startDate, endDate) => {
  const start = new Date(startDate);
  const end = new Date(endDate);
  return end > start;
}

const validateDescription = (description) => {
  return validateLenght(description, 500);
}

const validateTopic = (topic, otherTopic) => {
  if (topic == "Otro") {
    return validateLenght(otherTopic, 200) ;
  }
}
