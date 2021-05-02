<?php

ob_start();

function scanf($str)
{
    return fscanf(STDIN, $str);
}

class Queue
{
    private const SIZE = 1000;
    private $head = 0;
    private $tail = 0;
    private $arr = [];

    public function __construct()
    {
        $this->arr = array_fill(0, self::SIZE, null);
    }

    public function push($val)
    {
        $this->arr[$this->tail] = $val;
        $this->tail++;
        if ($this->tail == self::SIZE) {
            $this->tail = 0;
        }
    }

    public function front()
    {
        return $this->arr[$this->head];
    }

    public function pop()
    {
        $this->head++;
        if ($this->head == self::SIZE) {
            $this->head = 0;
        }
    }

    public function clean()
    {
        $this->head = 0;
        $this->tail = 0;
    }

    function empty() {
        return $this->head == $this->tail;
    }
}

class Pos
{
    public $r;
    public $c;
    public $w;

    public function __construct($r, $c, $w)
    {
        $this->r = $r;
        $this->c = $c;
        $this->w = $w;
    }
}
