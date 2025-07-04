package com.owoscarito.evaluaciones.model;

import jakarta.persistence.*;

@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "actividad_id", nullable = false)
    private Actividad actividad;

    @Column(name = "nota", nullable = false)
    private Integer nota;

    // Constructors
    public Nota() {}

    public Nota(Actividad actividad, Integer nota) {
        this.actividad = actividad;
        this.nota = nota;
    }

    // Getters and Setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public Actividad getActividad() { return actividad; }
    public void setActividad(Actividad actividad) { this.actividad = actividad; }

    public Integer getNota() { return nota; }
    public void setNota(Integer nota) { this.nota = nota; }
}