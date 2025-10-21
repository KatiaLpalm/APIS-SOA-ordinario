package com.example.apartamentos.repositories;

import com.example.apartamentos.models.Pago;

import org.springframework.data.jpa.repository.JpaRepository;



public interface IPagoRepository extends JpaRepository<Pago, Integer> {
  
}
