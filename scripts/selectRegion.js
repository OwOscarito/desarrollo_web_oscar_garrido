import region_comunas from "./region_comunas.js";

const selectRegion = document.getElementById("region");
const selectComuna = document.getElementById("comuna");

const populateRegions = () => {
    selectRegion.innerHTML = '<option value="">Seleccione una región</option>';
    region_comunas[regiones].forEach((region) => {
        const option = document.createElement("option");
        option.value = region.id;
        option.textContent = region.nombre;
        selectRegion.appendChild(option);
    });
};

const updateCommunes = () => {
    const selectedRegionId = selectRegion.value;
    selectComuna.innerHTML = '<option value="">Seleccione una comuna</option>';

    const selectedRegion = region_comunas.regiones.find(
        (region) => region.id === selectedRegionId
    );
    if (selectedRegion) {
        selectedRegion.comunas.forEach((comuna) => {
            const option = document.createElement("option");
            option.value = comuna.id;
            option.textContent = comuna.nombre;
            selectComuna.appendChild(option);
        });
    }
};

document.getElementById("select-region").addEventListener("change", updateCommunes);

window.onload = () => {
    populateRegions();
};
