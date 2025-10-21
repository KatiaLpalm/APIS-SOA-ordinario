package com.example.apartamentos.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.apartamentos.models.Disponibilidad;

@Repository
public interface IDisponibilidadRepository extends JpaRepository<Disponibilidad, Long> {

}
