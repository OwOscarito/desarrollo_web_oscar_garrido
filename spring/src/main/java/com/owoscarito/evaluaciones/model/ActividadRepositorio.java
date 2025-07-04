package com.owoscarito.evaluaciones.model;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ActividadRepositorio extends CrudRepository<Actividad, Integer> {
    Page<Actividad> findAllByOrderByIdDesc(Pageable pageable);
}