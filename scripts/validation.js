const validateLenght = (input, min_lenght, max_length) => {
  return  min_lenght <= input.length && input.length <= max_length;
};

const validateWhere = () => {
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
    return validateLenght(sector, 0, 100);
  }

  const selectRegion = document.getElementById("select-region").value;
  const selectCommune = document.getElementById("select-commune").value;
  const sector = document.getElementById("sector").value;

  if (!validateRegion(selectRegion)) {
    alert("Seleccione una región válida.");
    return false;
  };

  const selectCommuneValid = validateCommune(selectRegion, selectCommune);
  if (!selectCommuneValid) {
    alert("Seleccione una comuna válida.");
    return false;
  };

  const sectorValid = validateSector(sector);
  if (!sectorValid) {
    alert("Ingrese un sector válido.");
  return false;
  };
  return true;
};

const validateWho = () => {

  const validateName = (name) => {
    return validateLenght(name, 1, 200);
  };

  const validateEmail = (email) => {
    const emailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    return validateLenght(email, 1, 100) && emailRegex.test(email);
  };

  const validatePhoneNumber = (number) => {
    const phoneRegex = /^\+\d{3}\.\d{8}$/;
    return phoneRegex.test(number);
  };

  const validateContact = (contact) => {
    return validateLenght(contact, 0, 0) || validateLenght(contact, 4, 50);
  };

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phoneNumber = document.getElementById("phone").value;
  const whatsapp = document.getElementById("whatsapp").value;
  const telegram = document.getElementById("telegram").value;
  const instagram = document.getElementById("instagram").value;
  const tiktok = document.getElementById("tiktok").value;
  const x = document.getElementById("x").value;
  const other = document.getElementById("other").value;

  
  if (!validateName(name)) {
    alert("Ingrese un nombre válido.");
    return false;
  }

  if (!validateEmail(email)) {
    alert("Ingrese un correo electrónico válido.");
    return false;
  }

  if (!validatePhoneNumber(phoneNumber)) {
    alert("Ingrese un número de teléfono válido.");
    return false;
  }

  if (!validateContact(whatsapp)) {
    alert("Ingrese un contacto de WhatsApp válido.");
    return false;
  }
  if (!validateContact(telegram)) {
    alert("Ingrese un contacto de Telegram válido.");
    return false;
  }
  if (!validateContact(instagram)) {
    alert("Ingrese un contacto de Instagram válido.");
    return false;
  }
  if (!validateContact(tiktok)) {
    alert("Ingrese un contacto de TikTok válido.");
    return false;
  }
  if (!validateContact(x)) {
    alert("Ingrese un contacto de X válido.");
    return false;
  }
  if (!validateContact(other)) {
    alert("Ingrese un contacto adicional válido.");
    return false;
  }
  return true;
};

const validateWhen = () => {
  const validateDate = (date) => {
    // Regex for validating date in YYYY-MM-DD hh:mmformat
    const dateRegex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/;
    return dateRegex.test(date);
  };

  const validateEndDate = (startDate, endDate) => {
    if (!validateDate(endDate)) {
      return false;
    }
    const start = new Date(startDate);
    const end = new Date(endDate);
    return end > start;
  }

  const startDate = document.getElementById("start-datetime").value;
  const endCheckbox = document.getElementById("end-checkbox").value;
  const endDate = document.getElementById("end-datetime").value;

  if (!validateDate(startDate)) {
    alert("Ingrese una fecha de inicio válida.");
    return false;
  }
  if (!validateEndDate(startDate, endDate) && endCheckbox) {
    alert("Ingrese una fecha de término válida.");
    return false;
  }
  return true;
};

const validateWhat = () => {

  const validateDescription = (description) => {
    return validateLenght(description, 0, 500);
  }

  const validateTopic = (topic, otherTopic) => {
    if (topic == "Otro") {
      return validateLenght(otherTopic, 3, 15) ;
    } else {
      return topics.includes(topic);
    }
  }

  const description = document.getElementById("description").value;
  const topic = document.getElementById("select-topic").value;
  const otherTopic = document.getElementById("other-topic").value;

  if (!validateDescription(description)) {
    alert("Ingrese una descripción válida.");
    return false;
  }
  if (!validateTopic(topic, otherTopic)) {
    alert("Seleccione un tema válido.");
    return false;
  }
  return true;
};

const validateForm = () => {
  return validateWhere() && validateWho() && validateWhen() && validateWhat();
}
