package com.owoscarito.evaluaciones.controller;

import com.owoscarito.evaluaciones.service.ApiService;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {
    private final ApiService apiService;
    public ApiController(ApiService apiService) {
        this.apiService = apiService;

    }

    @GetMapping("/nota/{id}")
    public Map<String, String> getNota(@PathVariable Integer id) {
        return apiService.getNota(id);
    }

    @PostMapping("/nota/añadir")
    @ResponseBody
    public Map<String, String> addNota(@RequestParam("actividad-id") Integer actividadId,
                                       @RequestParam Integer nota) {
        Map<String, String> response = new HashMap<>();
        
        if (actividadId == null || nota == null) {
            response.put("status", "fail");
            response.put("error", "actividad-id and nota are required.");
            return response;
        } else if (nota < 1 || nota > 7) {
            response.put("status", "fail");
            response.put("error", "nota must be between 1 and 7.");
            return response;
        }
        
        return apiService.addNota(actividadId, nota);
    }
}
    
