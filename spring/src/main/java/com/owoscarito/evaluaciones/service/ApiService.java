package com.owoscarito.evaluaciones.service;

import com.owoscarito.evaluaciones.model.Actividad;
import com.owoscarito.evaluaciones.model.ActividadRepositorio;
import com.owoscarito.evaluaciones.model.Nota;
import com.owoscarito.evaluaciones.model.NotaRepositorio;
import org.springframework.stereotype.Service;



@Service
public class ApiService {
    private final ActividadRepositorio actividadRepositorio;
    private final NotaRepositorio notaRepositorio;
    public ApiService(ActividadRepositorio actividadRepositorio, NotaRepositorio notaRepositorio) {
        this.actividadRepositorio = actividadRepositorio;
        this.notaRepositorio = notaRepositorio;
    }
    public String getNota(Integer id) {
        return actividadRepositorio.findById(id)
            .orElseThrow(() -> new RuntimeException("Actividad not found"))
            .averageNota();
    }
    public String addNota(Integer actividadId, Integer nota) {
        Actividad a = actividadRepositorio.findById(actividadId)
                .orElseThrow(() -> new RuntimeException("Actividad not found"));
        Nota n = new Nota(a, nota);
        notaRepositorio.save(n);
        return "Nota agregada correctamente";
    }
}
