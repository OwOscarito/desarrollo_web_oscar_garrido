package com.owoscarito.evaluaciones.controller;

import org.springframework.ui.Model;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;
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
        List<Map<String, String>> actividadesData = appService.getDataActividades(0,5);
        System.out.println("------------------------Actividades Data: -----------------------" + actividadesData);
        model.addAttribute("data", actividadesData);
        return "evaluar";
    }

}
