package com.owoscarito.evaluaciones.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.validation.constraints.NotNull;
import org.springframework.web.multipart.MultipartFile;

import java.time.LocalDateTime;

@Entity
@Table(name = "actividad")
public class Actividad {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Long id;

    @NotNull
    private Long comuna_id;

    private String sector;

    @NotNull
    private String nombre;

    @NotNull
    private String email;

    private String celular;

    @NotNull
    private LocalDateTime dia_hora_inicio;

    @NotNull
    private LocalDateTime dia_hora_termino;

    private String descripcion;

    Actividad() {
        // Constructor por defecto
    }

    Actividad(Long comuna_id, String sector, String nombre, String email, String celular,
              LocalDateTime dia_hora_inicio, LocalDateTime dia_hora_termino, String descripcion) {
        this.comuna_id = comuna_id;
        this.sector = sector;
        this.nombre = nombre;
        this.email = email;
        this.celular = celular;
        this.dia_hora_inicio = dia_hora_inicio;
        this.dia_hora_termino = dia_hora_termino;
        this.descripcion = descripcion;
    }
    // Getters
    public Long getId() {
        return id;
    }

    public Long getComuna_id() {
        return comuna_id;
    }

    public String getSector() {
        return sector;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEmail() {
        return email;
    }

    public String getCelular() {
        return celular;
    }

    public LocalDateTime getDia_hora_inicio() {
        return dia_hora_inicio;
    }

    public LocalDateTime getDia_hora_termino() {
        return dia_hora_termino;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public static Boolean validateActivity(String confText, MultipartFile confImg) {
        // Ejercicio: implementar validacion de confesiones :)
        return true;
    }
}
