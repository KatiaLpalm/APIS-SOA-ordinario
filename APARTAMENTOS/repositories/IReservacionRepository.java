package com.example.apartamentos.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.apartamentos.models.Reservacion;

@Repository
public interface IReservacionRepository extends JpaRepository<Reservacion, Long> {

}
