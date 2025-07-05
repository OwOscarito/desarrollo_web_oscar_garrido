package com.owoscarito.evaluaciones.service;

import com.owoscarito.evaluaciones.model.Actividad;
import com.owoscarito.evaluaciones.model.ActividadRepositorio;
import com.owoscarito.evaluaciones.model.Nota;
import com.owoscarito.evaluaciones.model.NotaRepositorio;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@Service
public class ApiService {
    private final ActividadRepositorio actividadRepositorio;
    private final NotaRepositorio notaRepositorio;
    public ApiService(ActividadRepositorio actividadRepositorio, NotaRepositorio notaRepositorio) {
        this.actividadRepositorio = actividadRepositorio;
        this.notaRepositorio = notaRepositorio;
    }
    public Map<String, String> getNota(Integer actividadId) {
        Map<String, String> response = new HashMap<>();
        Optional<Actividad> actividadOptional = actividadRepositorio.findById(actividadId);
        
        if (actividadOptional.isPresent()) {
            Actividad a = actividadOptional.get();
            response.put("status", "success");
            response.put("nota", a.averageNota());
        } else {
            response.put("status", "fail");
            response.put("error", "Actividad not found");
        }
        
        return response;
    }

    public Map<String, String> addNota(Integer actividadId, Integer nota) {
        Map<String, String> response = new HashMap<>();
        
        try {
            Actividad a = actividadRepositorio.findById(actividadId)
                    .orElseThrow(() -> new RuntimeException("Actividad not found"));
            Nota n = new Nota(a, nota);
            notaRepositorio.save(n);
            
            response.put("status", "success");
            response.put("message", "Nota agregada correctamente");
        } catch (RuntimeException e) {
            response.put("status", "fail");
            response.put("error", e.getMessage());
        }
        
        return response;
    }
}
