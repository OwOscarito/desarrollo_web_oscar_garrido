package com.owoscarito.evaluaciones.controller;

import com.owoscarito.evaluaciones.service.ApiService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;

    }

    @GetMapping("/nota/{id}")
    public Double getNota(@PathVariable("id") Integer id) {
        return apiService.getNota(id);
    }

    @GetMapping("/nota/añadir")
    public String addNota(@RequestParam("actividad-id") Integer actividadId,
                          @RequestParam("nota") Integer nota) {
        if (actividadId == null || nota == null) {
            return "Error: actividad-id and nota are required.";
        } else if (nota < 1 || nota > 7) {
            return "Error: nota must be between 1 and 7.";
        }
        return apiService.addNota(actividadId, nota);
    }
}
    
