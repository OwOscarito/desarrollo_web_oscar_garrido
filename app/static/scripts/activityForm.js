const selectRegion = document.getElementById("select-region");
const selectCommune = document.getElementById("select-commune");

const populateRegions = () => {
  selectRegion.innerHTML = '<option value="">Seleccione una región</option>';
  region_comunas.regiones.forEach((region) => {
    const option = document.createElement("option");
    option.value = region.numero;
    option.textContent = region.nombre;
    selectRegion.appendChild(option);
  });
};

const updateCommunes = () => {
  const selectedRegionNumber = selectRegion.value;
  selectCommune.innerHTML = '<option value="">Seleccione una comuna</option>';

  const selectedRegion = region_comunas.regiones.find(
    (region) => region.numero == selectedRegionNumber
  );
  if (selectedRegion) {
    selectedRegion.comunas.forEach((comuna) => {
      const option = document.createElement("option");
      option.value = comuna.id;
      option.textContent = comuna.nombre;
      selectCommune.appendChild(option);
    });
  }
};

const populateDateTime = () => {
  let now = new Date();
  now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
  document.getElementById("start-datetime").value = now
    .toISOString()
    .slice(0, 16);
  const hourInMs = 60 * 60 * 1000;
  let end = new Date(now.getTime() + 3 * hourInMs);
  document.getElementById("end-datetime").value = end
    .toISOString()
    .slice(0, 16);
};

const populateTopics = () => {
  const selectTopic = document.getElementById("select-topic");
  selectTopic.innerHTML = '<option value="">Seleccione un tema</option>';
  topics.forEach((topic) => {
    const option = document.createElement("option");
    option.textContent = topic;
    selectTopic.appendChild(option);
  });
};

const updateOtherTopic = () => {
  if (document.getElementById("select-topic").value == "Otro") {
    document.getElementById("other-topic").style.display = "block";
  } else {
    document.getElementById("other-topic").style.display = "none";
  }
};

const validateAndSubmit = () => {
  if (validateForm()) {
    window.location.href = "index.html";
  }
}

document
  .getElementById("select-region")
  .addEventListener("change", updateCommunes);

document
  .getElementById("select-topic")
  .addEventListener("change", updateOtherTopic);

document
  .getElementById("submit-btn")
  .addEventListener("click", validateAndSubmit);


window.onload = () => {
  populateRegions();
  populateDateTime();
  populateTopics();
};
