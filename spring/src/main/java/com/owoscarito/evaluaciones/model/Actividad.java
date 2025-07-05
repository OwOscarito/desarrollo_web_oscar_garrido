package com.owoscarito.evaluaciones.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "actividad")
public class Actividad {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "sector", length = 100)
    private String sector;

    @Column(name = "nombre", nullable = false, length = 200)
    private String nombre;

    @Column(name = "dia_hora_inicio", nullable = false)
    private LocalDateTime diaHoraInicio;

    @Column(name = "dia_hora_termino")
    private LocalDateTime diaHoraTermino;

    @OneToMany(mappedBy = "actividad", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<ActividadTema> temas;

    @OneToMany(mappedBy = "actividad", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Nota> notas;

    Actividad() {
    }

    Actividad(Integer id, String sector, String nombre,
              LocalDateTime dia_hora_inicio, LocalDateTime dia_hora_termino,
              List<ActividadTema> temas, List<Nota> notas) {
        this.id = id;
        this.sector = sector;
        this.nombre = nombre;
        this.diaHoraInicio = dia_hora_inicio;
        this.diaHoraTermino = dia_hora_termino;
        this.temas = temas;
        this.notas = notas;
    }

    public Integer getId() {
        return id;
    }

    public List<ActividadTema> getTemas() {
        return temas;
    }

    public List<Nota> getNotas() {
        return notas;
    }

    public String getSector() {
        return sector;
    }

    public String getNombre() {
        return nombre;
    }

    public LocalDateTime getDiaHoraInicio() {
        return diaHoraInicio;
    }

    public LocalDateTime getDiaHoraTermino() {
        return diaHoraTermino;
    }

    public String averageNota() {
        if (notas == null || notas.isEmpty()) {
            return "-";
        }
        double total = 0.0;
        for (Nota nota : notas) {
            total += nota.getNota();
        }
        double result = total / notas.size();
        return String.format("%.1f", result);
    }

    public String stringTemas() {
        if (temas != null && !temas.isEmpty()) {
            StringBuilder strTemas = new StringBuilder();
            temas.forEach(tema -> {
                strTemas.append(tema.stringTema());
            });
            return strTemas.toString();
        }
        return "-";
    }
}
