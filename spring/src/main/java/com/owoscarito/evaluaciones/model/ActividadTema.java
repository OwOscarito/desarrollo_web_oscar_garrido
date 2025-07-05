package com.owoscarito.evaluaciones.model;

import jakarta.persistence.*;

enum Tema {
    música,
    deporte,
    ciencias,
    religión,
    política,
    tecnología,
    juegos,
    baile,
    comida,
    otro;
}

@Entity
@Table(name = "actividad_tema")
public class ActividadTema {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;

    //@NotNull
    @Enumerated(EnumType.STRING)
    private Tema tema;

    @Column(name = "glosa_otro")
    private String glosaOtro;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "actividad_id")
    private Actividad actividad;

    public Integer getId() {
        return id;
    }

    public String getGlosaOtro() {
        return glosaOtro;
    }

    public Actividad getActividad() {
        return actividad;
    }

    public void setActividad(Actividad actividad) {
        this.actividad = actividad;
    }

    public String stringTema() {
        System.out.println("ActividadTema.stringTema() tema: " + tema + ", glosaOtro: " + glosaOtro);
        if (tema == Tema.otro) {
            return glosaOtro;
        } else {
            return tema.toString();
        }
    }
}
