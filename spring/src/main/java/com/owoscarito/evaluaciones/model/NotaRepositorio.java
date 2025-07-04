package com.owoscarito.evaluaciones.model;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface NotaRepositorio extends CrudRepository<Nota, Integer> {

}