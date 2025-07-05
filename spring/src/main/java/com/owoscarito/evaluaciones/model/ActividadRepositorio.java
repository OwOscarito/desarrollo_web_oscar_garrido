package com.owoscarito.evaluaciones.model;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;


@Repository
public interface ActividadRepositorio extends CrudRepository<Actividad, Integer> {
    Page<Actividad> findByDiaHoraTerminoLessThanEqual(LocalDateTime diaHoraTermino, Pageable pageable);
}