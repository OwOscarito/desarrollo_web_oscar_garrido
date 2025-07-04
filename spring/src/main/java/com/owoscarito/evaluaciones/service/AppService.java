package com.owoscarito.evaluaciones.service;

import com.owoscarito.evaluaciones.model.Actividad;
import com.owoscarito.evaluaciones.model.ActividadRepositorio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.data.domain.PageRequest;

import java.util.List;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;


@Service
public class AppService {
    private final ActividadRepositorio actividadRepositorio;

    @Autowired
    public AppService(ActividadRepositorio actividadRepositorio) {
        this.actividadRepositorio = actividadRepositorio;
    }

    public List<Map<String, String>> getDataActividades(Integer pageNum, Integer pageSize) {
        LocalDateTime now = LocalDateTime.now();
        List<Actividad> actividades = actividadRepositorio.findByDiaHoraTerminoLessThanEqual(now, PageRequest.of(pageNum, pageSize)).getContent();
        System.out.println("---------------Actividades---------------" + actividades);
        List<Map<String, String>> data = new ArrayList<>(pageSize);

        actividades.forEach( actividad -> {
            Map<String, String> actividadData = new HashMap<>();

            actividadData.put("id", actividad.getId().toString());
            actividadData.put("sector", actividad.getSector());
            actividadData.put("nombre", actividad.getNombre());
            actividadData.put("inicio", actividad.getDiaHoraInicio().toString());
            actividadData.put("termino", actividad.getDiaHoraTermino() != null ? actividad.getDiaHoraTermino().toString() : "-");
            actividadData.put("temas", actividad.stringTemas());
            actividadData.put("nota", actividad.averageNota().toString());

            data.add(actividadData);
        });
        return data;
    }
}
