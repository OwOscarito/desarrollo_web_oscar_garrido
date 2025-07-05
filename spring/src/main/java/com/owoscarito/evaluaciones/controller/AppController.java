package com.owoscarito.evaluaciones.controller;

import org.springframework.ui.Model;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Map;

import com.owoscarito.evaluaciones.service.AppService;

@Controller
public class AppController {
    private final AppService appService;
    public AppController(AppService appService) {
        this.appService = appService;
    }

    @GetMapping("/base")
    public String baseRoute(Model model) {
        return "fragments/base";
    }

    @GetMapping("/")
    public String indexRoute(Model model) {
        return "redirect:/evaluar";
    }

    @GetMapping("/evaluar")
    public String evaluarRoute(Model model) {
        return evaluarByPageRoute(0, model);
    }

    @GetMapping("/evaluar/{page}")
    public String evaluarByPageRoute(@PathVariable Integer page, Model model) {
        Map<String, Object> result = appService.getDataActividades(page, 10);

        model.addAttribute("page", result.get("currentPage"));
        model.addAttribute("pageSize", result.get("pageSize"));
        model.addAttribute("pageCount", result.get("totalPages"));
        model.addAttribute("actividades", result.get("actividades"));
        
        return "evaluar";
    }

}
