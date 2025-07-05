package com.owoscarito.evaluaciones.service;

import com.owoscarito.evaluaciones.model.Actividad;
import com.owoscarito.evaluaciones.model.ActividadRepositorio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.data.domain.PageRequest;

import java.util.List;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
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
    String formatDateTime(LocalDateTime dateTime) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy\nHH:mm");
        return dateTime.format(formatter);
    }
    public List<Map<String, String>> getDataActividades(Integer pageNum, Integer pageSize) {
        LocalDateTime now = LocalDateTime.now();
        List<Actividad> actividades = actividadRepositorio.findByDiaHoraTerminoLessThanEqual(now, PageRequest.of(pageNum, pageSize)).getContent();
        //System.out.println("---------------Actividades---------------" + actividades);
        List<Map<String, String>> dataArray = new ArrayList<>(pageSize);

        actividades.forEach( actividad -> {
            //System.out.println("---------------Actividad---------------" + actividad);
            Map<String, String> data = new HashMap<>();

            data.put("id", actividad.getId().toString());
            data.put("sector", actividad.getSector());
            data.put("nombre", actividad.getNombre());
            data.put("inicio", formatDateTime(actividad.getDiaHoraInicio()));
            data.put("termino", actividad.getDiaHoraTermino() != null ? formatDateTime(actividad.getDiaHoraTermino()) : "-");
            data.put("temas", actividad.stringTemas());
            data.put("nota", actividad.averageNota());

            dataArray.add(data);
        });
        return dataArray;
    }
}
