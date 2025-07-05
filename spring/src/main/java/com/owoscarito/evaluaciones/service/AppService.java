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
    public Map<String, Object> getDataActividades(Integer pageNum, Integer pageSize) {
        LocalDateTime now = LocalDateTime.now();
        
        // Get paginated data
        var page = actividadRepositorio.findByDiaHoraTerminoLessThanEqual(now, PageRequest.of(pageNum, pageSize));
        List<Actividad> actividades = page.getContent();
        
        int totalPages = page.getTotalPages();
        
        List<Map<String, String>> actividadesData = new ArrayList<>(pageSize);

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

            actividadesData.add(data);
        });
        
        Map<String, Object> pageInfo = new HashMap<>();
        pageInfo.put("currentPage", pageNum);
        pageInfo.put("pageSize", pageSize);
        pageInfo.put("totalPages", totalPages);
        pageInfo.put("actividades", actividadesData);

        return pageInfo;
    }
}
