package com.example.apartamentos.repositories;

import com.example.apartamentos.models.Mensaje;
import org.springframework.data.jpa.repository.JpaRepository;

public interface IMensajeRepository extends JpaRepository<Mensaje, Integer> {
}
